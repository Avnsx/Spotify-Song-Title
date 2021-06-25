import pywinauto,psutil,random
from pywinauto.application import Application
from pywinauto import Desktop
from time import sleep as s

while True:
    try:
        mylist=[]
        for proc in psutil.process_iter():
            if proc.name() == 'Spotify.exe':
                mylist.append(proc.as_dict(attrs=['pid','num_threads'])) #windows only: 'num_handles'
        song_name_raw=[w.window_text() for w in Desktop(backend='uia').windows(process=int(max(mylist, key=lambda x: x['num_threads'])['pid']))][0]
    except:
        input('Spotify not found; Press Enter once you have started Spotify back up...')
        continue
    if song_name_raw not in ('Spotify Free', 'Spotify Premium'):
        song_name=str('Song: '+song_name_raw+' ♪')
        print(song_name)
        with open('song_name.txt', 'w', encoding='utf-8') as o:o.write(song_name)
    s(random.uniform(8,15))

