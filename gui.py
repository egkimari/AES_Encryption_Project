import tkinter as tk
from tkinter import messagebox
from encryption import generate_key, encrypt_message, decrypt_message
from otp_service import send_otp, get_key_from_otp

def encrypt_and_send():
    message = entry_message.get()
    phone = entry_phone.get()

    if not message or not phone:
        messagebox.showerror("Missing Info", "Enter both message and phone number.")
        return

    key = generate_key()
    encrypted = encrypt_message(message, key)
    send_otp(phone, key)

    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, f"Encrypted: {encrypted}\n\nOTP sent to {phone}")

def decrypt_msg():
    encrypted = entry_enc_msg.get()
    otp = entry_otp.get()

    key = get_key_from_otp(otp)

    if not key:
        messagebox.showerror("Invalid OTP", "No key found for that OTP.")
        return

    try:
        decrypted = decrypt_message(encrypted, key)
        text_decrypted.delete("1.0", tk.END)
        text_decrypted.insert(tk.END, f"Decrypted: {decrypted}")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# GUI window
app = tk.Tk()
app.title("AES Secure Messenger")
app.geometry("600x500")

# Encrypt section
tk.Label(app, text="Enter message to encrypt:").pack()
entry_message = tk.Entry(app, width=60)
entry_message.pack()

tk.Label(app, text="Enter phone number:").pack()
entry_phone = tk.Entry(app, width=30)
entry_phone.pack()

tk.Button(app, text="Encrypt & Send OTP", command=encrypt_and_send).pack(pady=10)
text_result = tk.Text(app, height=5)
text_result.pack()

# Decrypt section
tk.Label(app, text="\nPaste encrypted message:").pack()
entry_enc_msg = tk.Entry(app, width=60)
entry_enc_msg.pack()

tk.Label(app, text="Enter OTP:").pack()
entry_otp = tk.Entry(app, width=10)
entry_otp.pack()

tk.Button(app, text="Decrypt Message", command=decrypt_msg).pack(pady=10)
text_decrypted = tk.Text(app, height=5)
text_decrypted.pack()

app.mainloop()
