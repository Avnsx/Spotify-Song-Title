# spotify_song_name

# Description
On click screenreading software, to filter out your current spotify songs name, out of your window titles and creates a file named 'song_name.txt' in the same directory you downloaded the code in which has the song name in it as follows 'Song: I Got You Flowers! by LoveJSan ♪'.

This is pretty usefull if you're using OBS for example, you can just add a 'Text (GDI+)' Source into your current scene, and add the created 'song_name.txt' file location as source to that text, inside it's properties in OBS.

If it's not working properly and displaying another programs name, go to the source code into Line 6 (blacklist=[...]); and add a random word of the wrong found window in there, then restart the code.

# Known Bugs
Not fixable: If you're listening to a Song right now but your Spotify client is not on the '🏠 Start' page, you'll most likely experience lag, so make sure to set a song or a playlist first, then navigate back to the Start page(top left corner), to avoid this.

# Dependencies:
