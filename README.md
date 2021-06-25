# Spotify Song Title Reader
![GitHub Banner](https://repository-images.githubusercontent.com/334050272/9e9a3280-620b-11eb-883c-e4478e8cdfd8)
## Description
On click screenreading software(invisible in background), to crawl your current spotify songs name, out of your the Spotify Clients window Title which reveals the currently Song Title. It creates a file named ``song_name.txt`` in the same directory you launched the code from.
Once ran it will every 8-15 seconds(randomised) overwrite the recently created file, with the current song & artist name like in the following sample: ``Song: The Weeknd - The Hills ♪`` and also print it in the python console.

This is pretty usefull if you're using OBS for example, you can just add a 'Text (GDI+)' Source into your current scene and add the created file that will always contain the current songs title location as source to that text, inside it's properties in OBS.

## Dependencies

	pip install pywinauto
	pip install psutil
	pip install pywin32

Only if you get an error with win32api, you've to get the correct version(your python & OS version) of https://github.com/mhammond/pywin32/releases

## Additional Knowledge
I'm fully aware that there's an Spotify API that will exactly replicate the functionality of this code, but it requires you to run the official Spotify client, which I'm not doing, my Spotify user data is never going back to the Spotify Server, which makes it impossible for me to use their API. For everyone that has the same issue or just doesn't want to deal with their API, you're welcome to use this repo 🎉

Dependant on how many people show me that they're liking the code by giving ⭐'s on this repo, I'll expand functionality & push more quality of life updates.
