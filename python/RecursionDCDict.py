def recDC(List, change, knownResults):
    minCoins = change
    if change in List:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in List if c < change]:
            numCoins = 1 + recDC(List, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

print(recDC([1,5,10,25],63,[0]*64))

