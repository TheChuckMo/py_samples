#!/usr/bin/env python

# bundled python modules
import os

# The Python module for HTTP(S)
# http://docs.python-requests.org/en/master/
import requests

# URL: https://textfiles.com/bbs/BBSLISTS/026part1.lst (BBS Phone Numbers)
BBSLIST = 'https://textfiles.com/bbs/BBSLISTS/026part1.lst'

# Make a HTTP GET request to the URL
bbs = requests.get(BBSLIST, verify=False)
# bbs holds the response

# simple check if request successful
if bbs.ok:
    print( '.ok {} | .status_code {}'.format(bbs.ok, bbs.status_code) )
else:
    print( '.ok {} | .reason {}'.format(bbs.ok, bbs.reason) )

# Other parameters available
print('Headers Hash: {}'.format(bbs.headers))
print('Headers Date & Last Modified: {}/{}'.format(bbs.headers['Date'], bbs.headers['Last-Modified']))


# first 3 lines
print('First 3 lines of {}'.format(bbs.url))

# Split the ".text" string on lines into a List object (no variable name assigned)
# Loop on the first three objects from the List assigning each to line
# Print the string in line
for line in bbs.text.splitlines()[:3]:
    print(line)

# last 5 lines
print('Last 5 lines of {}'.format(bbs.url))

# Same as above, but use the last 5 items from the list
for line in bbs.text.splitlines()[-5:]:
    print(line)

# that was just some fun...

#
# write it to a file
#
# identify the directory of the script
# the "os" module allows to interact with the OS in an agnostic way
# will work regardless of OS it's running on.
# os.path.dirname(PATH) -> returns the directory name of a path (dropping filename)
# __file__ -> a python constant of the current file (the script)
# os.path.abspath(PATH) -> returns the absolute path of a file
# Use __file__ to find the absolute path of the script, then set the directory to SCRIPTDIR
SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))

# name our file and set it
# to stay OS agnostic, use python tools to combine paths - will make appropriate for filesystem/OS
# Combine the SCRIPTDIR and the filename for a valid path (proper "/\" and such...)
file = os.path.join(SCRIPTDIR, 'bbs_numbers.txt')

# write text from the response object to a local file.
# Instead of doing an open and close, we will use "with" to do it for use.
# open(filename, access) -> returns a file handle - access: 'r', 'w', and more...
# the with assigns the open file handle to open_file
# in the with we use open_file to write the String bbs.text to the file
# the file is closed when leaving the with.
print('Text written to file {}'.format(file))
with open(file, 'w') as open_file:
    open_file.write(bbs.text)

# Alternative
# open file handle
#open_file = open(file, 'w')
# write to file handle
#open_file.write(bbs.text)
# close the file
#open_file.close()


# close the request/response/connection
# there is no connection maintained, but we will close for good form.
# it is possible to reuse an open connection if making multiple requests.
bbs.close()
