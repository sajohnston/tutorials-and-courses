# Uses python3

def fibonacci(n):
    if n <= 1:
        return n
    
    fibs = [0, 1]
    for i in range(2, n+1):
        nextFib = fibs[i-1] + fibs[i-2]
        fibs.append(nextFib)

    return fibs[n]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))