import pytubefix
from pydub import AudioSegment
import os

url = input("Link: ")
user_choice = input("Video(V) or audio(A)?: ")
user_title = input("Name your file: ")
yt = pytubefix.YouTube(url)

if user_choice.capitalize() == 'A':
    print(f"Downloading audio for {yt.title}")
    os.rename(yt.streams.get_audio_only().download(), f"{user_title}0.m4a")
    AudioSegment.from_file(fr"C:\Users\{currentuser}\{user_title}0.m4a").export(fr"C:\Path\to\desired\folder{user_title}.mp3", format="mp3")
    os.remove(fr"{user_title}0.m4a")
else:
    print(f"Downloading video for {yt.title}")
    os.rename(yt.streams.get_highest_resolution().download(), f"{user_title}.mp4")
    os.rename(fr"C:\Users\{currentuser}\{user_title}.mp4", fr"C:\Path\to\desired\folder\v{user_title}.mp4")