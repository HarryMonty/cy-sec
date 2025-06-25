This project is to learn how to make a basic two-factor authentication system. It will be a basic script where a user logs in with a password and then confirms their identity using a second factor. This will be entirely done within python.

Some requirements are python libraries such as 'pyotp' 'qrcode' and an authenticator app. The script will be using a Hardcoded password, however in professional settings they are always encrypted into a hash string (seen in my 'encrypt-and-transfer project').

Relevant Files:

2fa-information.txt | Will hold the setup and important information
2fa-system.py | Python script for the 2fa system
qr_code.png | QR Code the python script creates for the 2fa authentication