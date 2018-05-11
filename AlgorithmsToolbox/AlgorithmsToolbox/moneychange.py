# Uses python3

def change_money(m):
    tens = m // 10
    fives = (m - (tens*10)) // 5
    ones = (m - (tens*10 + fives*5)) 
    return tens + fives + ones

if __name__ == "__main__":
    m = int(input())
    print(change_money(m))