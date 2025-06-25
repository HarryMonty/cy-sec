import pyotp
import qrcode

secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)
totpQR = totp.provisioning_uri(name="harry@localuser", issuer_name="CySecApp")
username = "admin"
password = "secure123"

userInput = input("Username: ").strip()
if userInput == username:
    passInput = input("Password: ").strip()
    if passInput == password:
        img = qrcode.make(totpQR)
        type(img)
        img.save("qr_code.png")

        otpInput = input("Please enter your 2FA code by scanning the QR Code: ")
        if totp.verify(otpInput):
            print("Success")
        else:
            print("Failure")
    else:
        print("Incorrect Password.")
else:
    print("Incorrect Username.")