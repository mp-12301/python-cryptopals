import binascii
import re

KEYSIZE_RANGES = range(2, 50)
FILENAME = 'cipher-text'


def hamming_distance_from_bits(s1, s2):
    bits_s1 = int(binascii.b2a_hex(s1), 16)
    bits_s2 = int(binascii.b2a_hex(s2), 16)
    return bin(bits_s1 ^ bits_s2).count("1")


def keysizes(filename):
    keysizes = []
    with open(filename) as f:
        # Decode from base64
        en = binascii.a2b_base64(f.read().replace('\n', ''))
        # KEYSIZE
        for keysize in KEYSIZE_RANGES:
            result = 0
            for i in range(keysize):
                result += hamming_distance_from_bits(en[i], en[keysize + i])
                result += hamming_distance_from_bits(en[keysize + i], en[2 * keysize + i])
                result += hamming_distance_from_bits(en[2 * keysize + i], en[3 * keysize + i])
                result += hamming_distance_from_bits(en[3 * keysize + i], en[4 * keysize + i])
            # print float(result) / float(keysize * 4), keysize
            keysizes.append((keysize, float(result) / float(keysize * 4)))
    keysizes.sort(key=lambda tup: tup[1])
    keysizes = [t[0] for t in keysizes]
    print keysizes
    return keysizes[:4]


def XOR_single(en, c):
    de = []
    for b in en:
        result = c ^ int(binascii.b2a_hex(b), 16)
        result = format(result, 'x')
        if len(result) == 1:
            result = '0' + result
        de.append(binascii.a2b_hex(result))
    return de


def check_score(listOfBytes):
    check = '[etaoinshrdluETAOINSHRDLU ]'
    count = 0
    for byte in listOfBytes:
        if re.match(check, byte):
            count += 1

    return count


# print hamming_distance_from_bits('this is a test', 'wokka wokka!!!')
keysizes = keysizes(FILENAME)
print keysizes

with open(FILENAME) as f:
    en = binascii.a2b_base64(f.read().replace('\n', ''))
    for keysize in keysizes:
        blocks = []
        for i in range(0, keysize):
            block = [en[j] for j in range(i, len(en), keysize)]
            for c in range(256):
                result = XOR_single(block, c)
                if check_score(result) * keysize > 1800:
                        print keysize, i, chr(c), check_score(result) * keysize
