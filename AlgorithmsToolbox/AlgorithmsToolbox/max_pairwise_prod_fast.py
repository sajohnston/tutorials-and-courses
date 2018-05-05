# Uses python3

import sys

def max_pairwise_product_fast(n, A):
    ind1 = 0
    for i in range(1, n):
        if A[i] > A[ind1]:
            ind1 = i
    if ind1 == 0:
        ind2 = 1
    else:
        ind2 = 0
    for i in range(1, n):
        if i != ind1 and A[i] > A[ind2]:
            ind2 = i
    prod = A[ind1] * A[ind2]
    return prod
 

if __name__ == "__main__":
    n = int(input())
    A = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(n, A))