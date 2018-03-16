from Crypto.Cipher import AES
import binascii

KEY = 'YELLOW SUBMARINE'
aes = AES.new(KEY, AES.MODE_ECB)

with open('cipher-text') as f:
    cipher_text = binascii.a2b_base64(f.read())
    print aes.decrypt(cipher_text)
