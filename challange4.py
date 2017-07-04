from challange3 import decode, evaluate

maybe = {}
with open("4.txt", "r") as input_file:
    for line in input_file:
        decoded = decode(line.strip("\n"))
        maybe[evaluate(decoded)] = decoded
    print maybe[max(maybe.keys())]
