from challange3 import encodeXOR

secret = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"


def repeating_key_xor(secret, key):
    e = ""
    lk = len(key)
    for position in range(len(secret) / lk):
        segment = secret[position * lk:position * lk + lk]
        print segment
        for char in range(lk):
            e += hex(ord(segment[char]) ^ ord(key[char])).replace("0x", "")
    print e
    print "b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


if __name__ == "__main__":
    repeating_key_xor(secret, key)
