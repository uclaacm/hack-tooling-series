import re
import webbrowser

YOUTUBE_REGULAR_EXPRESSION = '(youtube\.com\/watch\?v=.{11}|youtu\.be\/.{11})'

pattern = re.compile(YOUTUBE_REGULAR_EXPRESSION)

with open('messages.json', 'r') as message_file:
    contents = message_file.read()
    matches = re.findall(pattern, contents)
    print("Found these youtube videos:")
    print(matches)
    video_ids = []
    for match in matches:
        # long link https://www.youtube.com/watch?v=aBcDeFGH
        if ('v=') in match:
            video_ids.append(match.split('v=')[1])
        # short link https://youtu.be/aBcDeFGH
        if ('be/') in match:
            video_ids.append(match.split('be/')[1])
    playlist = 'http://www.youtube.com/watch_videos?video_ids=' + ','.join(video_ids)
    webbrowser.open(playlist)