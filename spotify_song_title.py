import pywinauto
from pywinauto.application import Application
from pywinauto import Desktop
from time import sleep as s

blacklist=['Google','Chrome','Sublime','Discord','obs64','OBS','Taskleiste','Taskbar','Firefox','Opera','Edge','Blitz','Lautstärkemixer','File','Explorer','Program','Manager','League','Launcher']

while True:
	window_titles=[w.window_text() for w in Desktop(backend="uia").windows()]
	best_guess = [f for f in window_titles if all([word not in f for word in blacklist])]
	for x in range (0,len(best_guess)):
		try:
			app_controls = Application(backend="uia").connect(title=best_guess[x])[best_guess[x]]
			split_s=best_guess[x].split(' - ')
			if split_s[1] or split_s[0] in str(app_controls.GroupBox.texts()[0]):
				song_name=str('Song: '+split_s[1]+' by '+split_s[0]+' ♪')
				print(song_name)
				with open('song_name.txt', 'w', encoding="utf-8") as output:output.write(song_name)
				s(10)
				break
		except:pass
