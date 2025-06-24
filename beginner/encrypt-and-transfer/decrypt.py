from cryptography.fernet import Fernet

keyRaw = open("sample-output/key.key")
key = (keyRaw.read())

tokenRaw = open("sample-output/secret.txt.encrypted")
token = (tokenRaw.read())

f = Fernet(key)
secret = f.decrypt(token)

with open("secret-decrypted.txt", "wb") as file:
    file.write(secret)