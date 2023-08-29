from pytube import YouTube
from sys import argv

weblink = argv[1]
yuTe = YouTube(weblink)

print("Title: ", yuTe.title)

print("View: ", yuTe.views)