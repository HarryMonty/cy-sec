from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("sample-output/key.key", "wb") as file:
    file.write(key)

f = Fernet(key)
token = f.encrypt(b"A really secret message.")

with open("sample-output/secret.txt.encrypted", "wb") as file:
    file.write(token)