#Código que baixa todos os videos de uma determinada playlist do youtube para mp3.
#Código "feito"(???) por Daniel Rabello

from pytube import Playlist
from pytube import YouTube
import os


url = []

playlist_url = Playlist('insert playlist link here')

for link in playlist_url:
    url.append(link)
    
for link in url:
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    pasta = r"insert folder here"
    
    output = video.download(output_path=pasta)
    
    base, ext = os.path.splitext(output)
    new_file = base + '.mp3'
    os.rename(output, new_file)
