#!/usr/bin/env python 

def count(s):
    letter_count = {}
    for letter in s:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

s = "Mississippi"
# the output order is unpredictable
print count(s)

letteritems = count(s).items()
letteritems.sort()
print letteritems

print sorted(count(s).items(), key=lambda x:x[1], reverse=True)


