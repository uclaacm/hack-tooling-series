#!/bin/bash
bookmarkCount=`grep -c "^$1 " bookmark.log`
if [ $bookmarkCount -gt 0 ]
    then
    open `grep "^$1 " bookmark.log | cut -d ' ' -f 2`
else
    echo "Bookmark not found"
fi
