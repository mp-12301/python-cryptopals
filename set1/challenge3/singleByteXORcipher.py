import string
import binascii
import re


def check_score(listOfBytes):
    check = '[etaoin shrdlu]'
    count = 0
    for byte in listOfBytes:
        if re.match(check, byte):
            count += 1
    return count


HEX_STRING_ENCRYPTED = '1b37373331363f78151b7f2b783431333d' \
    '78397828372d363c78373e783a393b3736'
CHARS = string.ascii_letters

encBytes = binascii.a2b_hex(HEX_STRING_ENCRYPTED)

plainTexts = []

for c in CHARS:
    plainText = []
    for b in encBytes:
        result = int(binascii.b2a_hex(c), 16) ^ int(binascii.b2a_hex(b), 16)
        result = format(result, 'x')
        if len(result) == 1:
            result = '0' + result
        plainText.append(binascii.a2b_hex(result))
    plainTexts.append(plainText)

for text in plainTexts:
    if check_score(text) > 5:
        print ''.join(text), check_score(text)
