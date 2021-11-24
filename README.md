# Spotify Song Title Reader
![Downloads](https://img.shields.io/github/downloads/Avnsx/Spotify-Song-Title/total?color=0078d7&label=🔽%20Downloads.exe&style=flat-square) ![Compatibility](https://img.shields.io/static/v1?style=flat-square&label=%F0%9F%90%8D%20Python&message=2.5%2B,%203%2B&color=blue) ![Stars](https://img.shields.io/github/stars/Avnsx/Spotify-Song-Title?style=flat-square&label=⭐%20Stars&color=ffc83d) [![Discord](https://img.shields.io/discord/522310203828338701?color=6A7EC2&label=Discord&logo=discord&logoColor=ffffff&style=flat-square)](https://discord.gg/Dr8wt84z2E)

![GitHub Banner](https://repository-images.githubusercontent.com/334050272/9e9a3280-620b-11eb-883c-e4478e8cdfd8)
## Description
One click code, to crawl your current spotify songs name & artist, out of the Spotify clients window title. It creates a file named ``song_name.txt`` in the same directory you launched the code from, which will contain the information.
Once ran it will every 8-15 seconds(randomised) overwrite the recently created file, with the current song & artist name like in the following sample: ``Song: The Weeknd - The Hills ♪`` and also print it in the python console.

This is pretty usefull if you're using OBS for example, you can just add a 'Text (GDI+)' Source into your current scene and add the created file that will always contain the current songs title location as source to that text, inside it's properties in OBS.

## Installation
You can just install the [Executable version](https://github.com/Avnsx/Spotify-Song-Title/releases)

Else you'll need to install python and the dependencies below through python.

## Dependencies
If you are using the raw source, paste below in cmd:

	pip install pywinauto psutil pywin32

Only if you get an error with win32api, you've to get the correct version(your python & OS version) of https://github.com/mhammond/pywin32/releases

## Additional Knowledge
I'm fully aware that there's an Spotify API that will exactly replicate the functionality of this code, but it requires you to run the official Spotify client, which I'm not doing, my Spotify user data is never going back to the Spotify Server, which makes it impossible for me to use their API. For everyone that has the same issue or just doesn't want to deal with their API, you're welcome to use this repo 🎉

Dependant on how many people show me that they're liking the code by giving ⭐'s on this repo, I'll expand functionality & push more quality of life updates.

