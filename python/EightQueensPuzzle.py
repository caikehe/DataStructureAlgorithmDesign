#!/usr/bin/env python 

def share_diagonal(x0,y0,x1,y1):
    #check if (x0, y0) shares diagonal with (x1,y1)
    dy = abs(y1-y0)
    dx = abs(x1-x0)
    return dx == dy

# check if the queen at column c clashes with any queen to its left
def col_clashes(bs, c):
    for i in xrange(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False

def has_clashes(the_board):
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    import random
    rng = random.Random()
    # generate the initial permutation
    bd = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 30:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1

main()
















