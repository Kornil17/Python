import wheel, steganocryptopy


# with password
from steganocryptopy.steganography import Steganography
Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "secret.png", "secrete_message.txt")
secret.save("secret2.png")

result = Steganography.decrypt("key.key", "secret2.png")
print(result)


# just secret.png
# from stegano import lsb
#
# secret = lsb.hide("/home/kornil/Загрузки/test.png", "your password: 1234")
# secret.save("secret.png")
#
# result = lsb.reveal("secret.png")
# print(result)

