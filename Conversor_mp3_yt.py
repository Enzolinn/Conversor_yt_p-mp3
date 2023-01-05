from pytube import YouTube
import moviepy.editor as mp
import re
import os

# digite o link do vid e o endereço onde quer salvar
link = input("link do video por favor: ")
path=input("digite o endereço de onde quer salvar o arquivo: ")

yt = YouTube(link)

print("baixando...")
ys= yt.streams.filter(only_audio=True).first().download(path)
print("download completo.")

print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucesso.')
