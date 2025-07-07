import requests
import random
import base64
import json
import os

# Infobip credentials
API_KEY = "App 98bf37d282f6fd41b783737783700ccd-efb34e20-3e74-4d8c-ac0c-5aa6f2739e07"
BASE_URL = "https://api.infobip.com/sms/2/text/advanced"

# Path to the file that stores OTP -> AES key mappings
OTP_STORE = "otp_keys.json"

# Generate random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Save AES key (as base64 string) linked to OTP
def save_key(otp, key_bytes):
    # Load existing data or create new
    if os.path.exists(OTP_STORE):
        with open(OTP_STORE, "r") as f:
            otp_map = json.load(f)
    else:
        otp_map = {}

    # Save AES key (encoded as base64 string)
    otp_map[otp] = base64.b64encode(key_bytes).decode()

    # Write back to file
    with open(OTP_STORE, "w") as f:
        json.dump(otp_map, f)

# Retrieve AES key using OTP
def get_key_from_otp(otp):
    if not os.path.exists(OTP_STORE):
        return None

    with open(OTP_STORE, "r") as f:
        otp_map = json.load(f)

    key_b64 = otp_map.get(otp)
    if key_b64:
        return base64.b64decode(key_b64)

    return None

# Send OTP via SMS and save AES key
def send_otp(phone_number, aes_key_bytes):
    otp = generate_otp()
    save_key(otp, aes_key_bytes)

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "messages": [
            {
                "from": "AESApp",
                "destinations": [{"to": phone_number}],
                "text": f"Your AES OTP is: {otp}"
            }
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        print("OTP sent via Infobip SMS!")
        print("Response:", response.json())
    except Exception as e:
        print(" Failed to send OTP via Infobip.")
        print("Error:", e)
