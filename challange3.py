freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}
nonprintables = [i for i in range(0, 31)]


def encodeXOR(m, key):
    d = ""
    for x in range(len(m)):
        d += chr(ord(m[x]) ^ key)
    return d


def decode(message):
    m = message.decode("hex")
    maybe = {}
    for key in range(0xFF):
        d = encodeXOR(m, key)
        print d
        score = evaluate(d)
        # if score > 0:
        maybe[score] = d
    return maybe[max(maybe.keys())]


def evaluate(frase):
    score = 0
    for letter in frase:
        for char in freqs:
            if letter == char:
                score += freqs[char]
        for char in nonprintables:
            if letter == chr(char):
                score -= 1
    return score


if __name__ == "__main__":
    print decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
