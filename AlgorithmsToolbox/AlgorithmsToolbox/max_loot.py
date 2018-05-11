# Uses python3
import sys

def max_loot(n, maxWeight, infoItems):
    bag_value = 0
    used_weight = 0 
    items_left = n
    while used_weight < maxWeight and items_left > 0:
        max_ind = 0
        for i in range(1, len(infoItems)):
            curr_max_val_per_weight = infoItems[max_ind][0] / infoItems[max_ind][1]
            val_per_weight_i = infoItems[i][0] / infoItems[i][1]
            if curr_max_val_per_weight < val_per_weight_i:
                max_ind = i
        max_val = infoItems[max_ind][0]
        max_val_weight = infoItems[max_ind][1]
        remain_weight = maxWeight - used_weight
        if max_val_weight <= remain_weight:
            bag_value += max_val
            used_weight += max_val_weight
        else:
            bag_value += (max_val / max_val_weight) * remain_weight
            used_weight += remain_weight
        del infoItems[max_ind]
        items_left = len(infoItems)

    return float("{0:.4f}".format(bag_value))


if __name__ == "__main__":
    nW = input().split()
    n = int(nW[0])
    W = int(nW[1])
    items = [[] for i in range(n)]
    for i in range(0, n):
        items[i] = [int(x) for x in input().split()]
    print(max_loot(n, W, items))