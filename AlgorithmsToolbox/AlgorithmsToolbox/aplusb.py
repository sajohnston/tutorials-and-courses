# Uses python3

import sys

def sum_single_digits(a, b):
    return a + b

if __name__ == "__main__":
    inp = sys.stdin.read()
    tokens = inp.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(sum_single_digits(a, b))