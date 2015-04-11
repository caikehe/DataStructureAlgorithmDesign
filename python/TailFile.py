#! /usr/bin/env python 

import time
def tail(f):
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0)
            continue
        yield line

def grep(lines, text):
    for line in lines:
        if text in line:
            yield line


tt = tail(open('text.txt'))
line = grep(tt, 'for')
for l in line:
    print l

