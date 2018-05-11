
def max_ad_revenue(a, b):
    max_rev = 0

    while len(a) > 0:
        ind_a = 0
        ind_b = 0
        for i in range(1, len(a)):
            if (a[ind_a] < a[i]):
                ind_a = i
            if (b[ind_b] < b[i]):
                ind_b = i
        max_rev += a[ind_a] * b[ind_b]
        del a[ind_a]
        del b[ind_b]

    return max_rev