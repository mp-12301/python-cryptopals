import binascii
import re


def check_score(listOfBytes):
    check = '[etaoinshrdluETAOINSHRDLU ]'
    count = 0
    for byte in listOfBytes:
        if re.match(check, byte):
            count += 1

    return count


def XOR_single(en, c):
    de = []
    for b in en:
        result = c ^ int(binascii.b2a_hex(b), 16)
        result = format(result, 'x')
        if len(result) == 1:
            result = '0' + result
        de.append(binascii.a2b_hex(result))
    return de


with open('text') as f:
    for line in f:
        en = binascii.a2b_hex(line.rstrip())
        for c in range(256):
            de = XOR_single(en, c)
            if check_score(de) > 16:
                print check_score(de), chr(c), line.rstrip()
                print '############'
                print ''.join(de)
                print '############'
