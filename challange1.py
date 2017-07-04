import _codecs


def hextob64(hex_string):
    hex_data = hex_string.decode("hex")
    b64 = _codecs.encode(hex_data, "base64")
    print(hex_data)
    return b64


hextob64(hex_string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
