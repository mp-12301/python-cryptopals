import binascii

hexString = raw_input('Enter the hex string: ')
binary = binascii.a2b_hex(hexString)
base64String = binascii.b2a_base64(binary)
print base64String
