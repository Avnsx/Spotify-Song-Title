# Spotify Song Name Reader
![GitHub Banner](https://repository-images.githubusercontent.com/334050272/9e9a3280-620b-11eb-883c-e4478e8cdfd8)
## Description
On click screenreading software, to filter out your current spotify songs name, out of your Spotify Client and then creates a file named 'song_name.txt' in the same directory you launched the code from. Once ran it will every 10 seconds overwrite the recently created file, with the current song & artist name like the following sample: 'Song: Boy Meets World by SANTANA ALI ♪' and also print it in the python console.

This is pretty usefull if you're using OBS for example, you can just add a 'Text (GDI+)' Source into your current scene, and add the created 'song_name.txt' file location as source to that text, inside it's properties in OBS.

If it's not working properly and displaying another programs name, go to the source code into Line 6 (blacklist=[...]); and add a random word of the wrong found window in there, then restart the code.

If you wish to lower the time it looks for an new song, go edit line 19 where it says 's(10)' and edit the interger '10' to whatever time you wish in seconds.

## Known Bugs
Not fixable: If you're listening to a Song right now but your Spotify client is not on the '🏠 Start' page, you'll most likely experience lag, so make sure to set a song or a playlist first, then navigate back to the Start page(top left corner), to avoid this.
If there's anything apart from this let me know in repo > issues.

## Dependencies:

	pip install pywinauto

and also dependant on your python version and os version get the correct version of https://github.com/mhammond/pywin32/releases

## Additional Knowledge:
I'm fully aware that there's an Spotify API that will exactly replicate the functionality of this code, but it requires you to run the official Spotify client, which I'm not doing, my Spotify user data is never going back to the Spotify Server, which makes it impossible for me to use their API.
