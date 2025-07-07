from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def generate_key():
    return get_random_bytes(16)

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message)
    encrypted = cipher.encrypt(padded.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(encrypted_message)
    decrypted = cipher.decrypt(decoded).decode()
    return decrypted.strip()
