def xor(h1, h2):
    return (h1 ^ h2)


hex1 = 0x1c0111001f010100061a024b53535009181c
hex2 = 0x686974207468652062756c6c277320657965

print(hex(xor(hex1, hex2)))