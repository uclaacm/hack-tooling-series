# Hack Tooling Series - Regular Expressions

**Date**: May 14, 2020\
**Location**: Zoom\
**Teachers**: Timothy Gu, Kristie Lim

## Resources

**Slides**

- [Slides](https://tinyurl.com/tooling-6)

**ACM Membership Attendance Portal**

- [Portal](https://members.uclaacm.com/login)

**Resources**

- [RegExr: A Regular Expression Tester](https://regexr.com/)
- [Cheatsheet](https://www.rexegg.com/regex-quickstart.html)
- [Dive Into Python RegEx Tutorial](https://diveintopython3.net/regular-expressions.html)

## Why Regular Expressions?

## Common Regular Expression Techniques

- `.`: matches any letter
- `a`: matches the letter `a`
- `^` and `$`: matches the beginning and end of line, respectively
- `a*`: matches zero or more letters `a`
- `a+`: matches one or more letters `a`
- `a?`: matches zero or one `a`
- `a{n,m}`: matches between n and m occurrences of `a`
- `[a-z123]`: matches a lower-case letter, or `1`, or `2`, or `3`
- `abc|def`: matches `abc` or `def` 
- `a(bc|de)f`: matches `abcf` or `adef`

## Theory

## Mini Project

Get a playlist of youtube links from your Facebook messages to someone! Try to write your own program first, but a sample python implementation is found in `get_youtube_links.py`.

A sample set of messages is found in `messages.json`. There are 7 links you can try to match there.

If you want to do this with your own Facebook messages, go to "Settings" > "Your Facebook Information". Then click "Download Your Information." Uncheck everything except messages. Choose your preferred date range, JSON format and low media quality. After requesting, you can go to the "Available Copies" tab to see your pending copy. It will take some time before it is available. 

This mini project is based off of https://medium.com/@julianknodt/converting-fb-messages-into-a-youtube-playlist-using-nodejs-aba60156ea72.