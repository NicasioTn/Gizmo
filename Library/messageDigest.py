import hashlib
import qrcode


class MessageDigest:
    def md5(self, data):
        return hashlib.md5(data.encode()).hexdigest()

    def sha1(self, data):
        return hashlib.sha1(data.encode()).hexdigest()

    def sha224(self, data):
        return hashlib.sha224(data.encode()).hexdigest()

    def sha256(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def sha384(self, data):
        return hashlib.sha384(data.encode()).hexdigest()

    def sha512(self, data):
        return hashlib.sha512(data.encode()).hexdigest()

    def sha3_224(self, data):
        return hashlib.sha3_224(data.encode()).hexdigest()

    def sha3_256(self, data):
        return hashlib.sha3_256(data.encode()).hexdigest()

    def sha3_384(self, data):
        return hashlib.sha3_384(data.encode()).hexdigest()

    def sha3_512(self, data):
        return hashlib.sha3_512(data.encode()).hexdigest()

message = "Hello, World!"
md = MessageDigest()
print("Message:", message)
print("MD5:", md.md5(message))
print("SHA-1:", md.sha1(message))
print("SHA-224:", md.sha224(message))
print("SHA-256:", md.sha256(message))
print("SHA-384:", md.sha384(message))
print("SHA-512:", md.sha512(message))
print("SHA-3-224:", md.sha3_224(message))
print("SHA-3-256:", md.sha3_256(message))
print("SHA-3-384:", md.sha3_384(message))
print("SHA-3-512:", md.sha3_512(message))

if __name__ == "__main__":
    # import qrcode
    # import qrcode.image.svg
    # factory = qrcode.image.svg.SvgPathImage
    # img = qrcode.make(message, image_factory=factory)
    # img.save("qrcode.svg")

    data = md.sha3_512(message)

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Sha3_512.png")