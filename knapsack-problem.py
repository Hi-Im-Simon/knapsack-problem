def knapsack(rows, wei, val):
    cols = len(val)
    tab = [[0 for _ in range(rows + 1)] for _ in range(cols + 1)]

    for row in range(cols + 1):
        for col in range(rows + 1):
            if row == 0 or col == 0:
                tab[row][col] = 0
            elif wei[row-1] <= col:
                tab[row][col] = max(val[row-1] + tab[row-1][col-wei[row-1]], tab[row-1][col])
            else:
                tab[row][col] = tab[row-1][col]
    return tab[cols][rows]


# generator
import random as ran
import time

for _ in range(10):
    BAG_SIZE = 10000
    ITEM_COUNT = 1000
    values = []
    weights = []    

    for _ in range(int(ITEM_COUNT)):
        rand = ran.randint(1, 100)
        weights.append(rand)
        values.append(rand * ran.randint(1, 5))

    start = time.time()
    knapsack(BAG_SIZE, weights, values)
    print(time.time() - start)
