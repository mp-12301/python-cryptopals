import binascii
from sys import argv

KEY = 'Terminator X: Bring the noise'

with open('input') as f:
    i = 0
    enBytes = []
    for line in f:
        if '-de' in argv:
            line = binascii.a2b_hex(line)
        for byte in line:
            keyIndex = i % len(KEY)
            en = ord(byte) ^ ord(KEY[keyIndex])
            enBytes.append(chr(en))
            i += 1
if '-de' in argv:
    print ''.join(enBytes)
else:
    print binascii.b2a_hex(''.join(enBytes))
