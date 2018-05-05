# Uses python3

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    fibsLast = [0, 1]
    for i in range(2, n+1):
        nextFibLast = (fibsLast[i-1] + fibsLast[i-2]) % 10
        fibsLast.append(nextFibLast)

    return fibsLast[n]
