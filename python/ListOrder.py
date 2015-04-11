#!/usr/bin/env python 
import sys

ls = []
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break
    line_split = line.split(" ")
    # line_split is list (it can be translated to tuple)
    #ls.append((line_split[0], line_split[1]))
    ls.append(line_split)

ls_sorted = sorted(ls, key = lambda x:x[1], reverse = True)

for item in ls_sorted:
    print item[0], item[1]
