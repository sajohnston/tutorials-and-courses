# Uses python3
import sys
import numpy

# For the assignment, we're copying the function here rather than importing
def gcd(a,b):
    if b == 0:
        return a
    aP = a % b
    return gcd(b, aP)

def lcm(a, b):
    q = gcd(a, b)
    m = (a // q) * b
    return int(m)

if __name__ == "__main__":
    inp = sys.stdin.read()
    tokens = inp.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(lcm(a, b))