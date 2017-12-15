#!/usr/bin/env python

# The Python module for HTTP(S)
# http://docs.python-requests.org/en/master/
import requests

# URL: https://textfiles.com/bbs/BBSLISTS/026part1.lst (BBS Phone Numbers)
BBSLIST = 'https://textfiles.com/bbs/BBSLISTS/026part1.lst'
bbs = requests.get(BBSLIST)


