import binascii

with open('cipher-text') as f:

    line = f.readline()[:-1]

    while(line):
        cipher_text = binascii.a2b_hex(line)
        count = 0
        for i in range(0, len(cipher_text), 16):
            word = cipher_text[i:i+16]
            for j in range(i+16, len(cipher_text), 16):
                if word == cipher_text[j:j+16]:
                    count += 1
        if count > 0:
            print count, line, cipher_text
        line = f.readline()[:-1]
