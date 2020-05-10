import re

YOUTUBE_REGULAR_EXPRESSION = 'youtube.com'

pattern = re.compile(YOUTUBE_REGULAR_EXPRESSION)

with open('messages.json', 'r') as message_file:
    contents = message_file.read()
    matches = re.findall(pattern, contents)
    print(matches)