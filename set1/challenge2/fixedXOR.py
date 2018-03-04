import binascii

HEX_TO_CHECK_AGAISNT = '686974207468652062756c6c277320657965'

hexStringReceived = raw_input('Hex string: ')
result = int(hexStringReceived, 16) ^ int(HEX_TO_CHECK_AGAISNT, 16)

# Format int to hex string
resultInHex = format(result, 'x')

print resultInHex
print binascii.a2b_hex(resultInHex)
