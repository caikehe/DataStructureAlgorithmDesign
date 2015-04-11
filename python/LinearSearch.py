#!/usr/bin/env python 

def linearSearch(arr, target):
    for (i,v) in enumerate(arr):
        if v==target:
            return i
    return -1

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (linearSearch(vocab, w) < 0):
            result.append(w)
    return result

vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
print find_unknown_words(vocab, book_words)
