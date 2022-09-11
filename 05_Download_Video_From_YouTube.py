# Download pytube library

from pytube import YouTube

link = input("Enter YouTube link:")

yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Views: {yt.views}")

yd = yt.streams.get_highest_resolution()

yd.download("C:\\Users\\hp\\Google Drive\\R&D\\Python\\Machine_Learning\\OpenCV Full Course 2022\\Download Video")



