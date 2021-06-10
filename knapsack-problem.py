class Knapsack:
    def __init__(self, cols, wei, val):
        self.cols = cols
        self.wei = wei
        self.val = val
        self.rows = len(val)
        self.tab = [[0 for _ in range(cols + 1)] for _ in range(self.rows + 1)]

        for row in range(self.rows + 1):
            for col in range(cols + 1):
                if row == 0 or col == 0:
                    self.tab[row][col] = 0
                elif wei[row-1] <= col:
                    self.tab[row][col] = max(val[row-1] + self.tab[row-1][col-wei[row-1]], self.tab[row-1][col])
                else:
                    self.tab[row][col] = self.tab[row-1][col]

    
    def findMaxValue(self, bag_size):
        if bag_size <= self.cols:
            return self.tab[self.rows][bag_size]
        return 'Knapsack size too large'


    def findElements(self, bag_size):
        if bag_size <= self.cols:
            return self.findNext(bag_size, self.rows, [])
        return 'Knapsack size too large'


    def findNext(self, x, y, elems):
        if y > 0 and x > 0:
            if self.tab[y][x] == self.tab[y-1][x]:
                self.findNext(x, y-1, elems)
            else:
                elems.append(self.val[y-1])
                self.findNext(x-self.wei[y-1], y-1, elems)
        return elems


# Generator
import random as ran
import time

for _ in range(1):
    BAG_SIZE = 1000
    ITEM_COUNT = 100
    values = []
    weights = []    

    for _ in range(int(ITEM_COUNT)):
        rand = ran.randint(1, 100)
        weights.append(rand)
        values.append(rand * ran.randint(1, 5))

    start = time.time()
    ks = Knapsack(BAG_SIZE, weights, values)
    print(time.time() - start)

    # You can use any value from 1 to BAG_SIZE
    print(ks.findMaxValue(BAG_SIZE))
    print(ks.findElements(BAG_SIZE))
