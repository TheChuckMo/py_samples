#!/usr/bin/env python

# bundled python modules
import os

# The Python module for HTTP(S)
# http://docs.python-requests.org/en/master/
import requests

# URL: https://textfiles.com/bbs/BBSLISTS/026part1.lst (BBS Phone Numbers)
BBSLIST = 'https://textfiles.com/bbs/BBSLISTS/026part1.lst'

# Make a GET request to the URL
# The results be returned as Dictionary
bbs = requests.get(BBSLIST, verify=False)

# Status Code of the Request bbs.status_code
print('Status Code: {}'.format(bbs.status_code))

# Headers are available
print('Headers Hash: {}'.format(bbs.headers))
print('Headers Date & Last Modified: {}/{}'.format(bbs.headers['Date'], bbs.headers['Last-Modified']))

#print text from url
#print('URL Text {}'.format(bbs.text))

# first 10 lines
print('First 3 lines of {}'.format(bbs.url))
for line in bbs.text.splitlines()[:3]:
    print(line)

# last 10 lines
print('Last 5 lines of {}'.format(bbs.url))
for line in bbs.text.splitlines()[-5:]:
    print(line)

#
# write it to a file
#
# identify the directory of the script
SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))

# name our file and set it
file = os.path.join(SCRIPTDIR, 'bbs_numbers.txt')

# open file for write
with open(file, 'w') as open_file:
    open_file.write(bbs.text)

print('Numbers written to {}'.format(file))
