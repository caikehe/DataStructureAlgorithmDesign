# recursively make change
def recMC(List, change):
    if change in List:
        return 1
    #the maximum number of change is "change"
    minChange = change
    for i in [c for c in List if c < change]:
        tmp = 1 + recMC(List, change-i)
        if tmp < minChange:
            minChange = tmp

    return minChange


List = [1, 5, 10, 25]
print recMC(List, 63)
