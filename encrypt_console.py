# Import AES key generation and encryption
from encryption import generate_key, encrypt_message
# Import secure OTP sending and mapping
from otp_service import send_otp
import base64

# Step 1: Get the message from the user
message = input("Enter the message to encrypt: ")

# Step 2: Generate AES key (16 bytes for AES-128)
key = generate_key()

# Step 3: Encrypt the message using AES
encrypted_msg = encrypt_message(message, key)

# Step 4: Get recipient's number
receiver_number = input("Enter the phone number: ")

# Step 5: Send OTP to that number, internally mapping it to the AES key
send_otp(receiver_number, key)

# Step 6: Show encrypted message
print("\n Encrypted Message:")
print(encrypted_msg)
print("\n Done!")
