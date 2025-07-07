from encryption import decrypt_message
from otp_service import get_key_from_otp

# Ask user for encrypted message and OTP
encrypted_msg = input("Paste the encrypted message: ")
otp = input("Enter the OTP (6-digit code sent via SMS): ")

# Fetch AES key from saved OTP-Key map
key = get_key_from_otp(otp)

if key:
    try:
        decrypted = decrypt_message(encrypted_msg, key)
        print("\n Decrypted Message:", decrypted)
    except Exception as e:
        print("Failed to decrypt.")
        print("Error:", e)
else:
    print("Invalid or expired OTP.")
