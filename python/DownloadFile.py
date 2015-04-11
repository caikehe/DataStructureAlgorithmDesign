#!/usr/bin/env python

import urllib2
resp = urllib2.urlopen("http://openbookproject.net/thinkcs/python/english3e/_downloads/alice_in_wonderland.txt")
html = resp.read()
outfile = open('text.txt','wb')
outfile.write(html)
outfile.close()


