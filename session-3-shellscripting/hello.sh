#!/bin/bash
echo "Hello world!"
echo "Hello $1!"
echo 'Hello $1!' # This will print Hello $1!
name=$1
echo "Hello $name!"

# check if argument is found in bookmark.log
if [ `grep -c "^$1 " bookmark.log` -gt 0 ]
	then
	# replace all instances of the bookmark name with open
	# then run in bash
	grep "^$1 " bookmark.log | sed "s/$1/open/" | bash
else
	echo "Bookmark not found"
fi