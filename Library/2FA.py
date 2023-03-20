import time
import pyotp
import qrcode
import qrcode.image.svg

class TwoFactorAuth:
    
    #key = pyotp.random_base32()
    #print("Your secret key is: " + key)
    counter = 0
    
    def __init__(self):
        self.key = "NetworkSecurity"
        self.hotp = pyotp.HOTP(self.key)
        self.totp = pyotp.TOTP(self.key)
        
    def input_code(self):
        return input("Enter the 2FA code: ")
        
    def show2FACode(self, type):
        if type is "totp":
            print("Current OTP is TOTP: " + self.totp.now())
        else:
            print("Current OTP is HOTP: " + self.hotp.at(count=self.counter))

    def verifyHOTP(self, code, counter):
        for _ in range(5):
            
            if self.hotp.verify(code, counter) == True:
                print(self.hotp.verify(code, counter), end=" /")
            else:
                print(self.hotp.verify(code, counter), end=" X")
            print()
            counter += 1
            
    def verifyTOTP(self, code):
        if self.totp.verify(code) == True:
            print("Correct code")
        else:
            print("Incorrect code")
    
    def QRCode(self):
        uri = pyotp.totp.TOTP(self.key).provisioning_uri(name="NetworkSecurity", 
                                                         issuer_name="NetworkSecurity APP")
        print(uri)
        qrcode.make(uri).save("12FA.png")

def main():
    the2FA = TwoFactorAuth()
    the2FA.show2FACode("totp")
    # the2FA.show2FACode("hotp")
    the2FA.verifyTOTP(the2FA.input_code())
    #the2FA.verifyHOTP(the2FA.input_code(), the2FA.counter)
    # the2FA.QRCode()
    
if __name__ == "__main__":
    main()


