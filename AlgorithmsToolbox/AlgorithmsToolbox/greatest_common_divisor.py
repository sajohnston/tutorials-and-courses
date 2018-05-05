# Uses python3

def gcd(a,b):
    if b == 0:
        return a
    aP = a % b
    return gcd(b, aP)


if __name__ == "__main__":
    inp = sys.stdin.read()
    tokens = inp.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(gcd(a, b))