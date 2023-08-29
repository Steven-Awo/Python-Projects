from pytube import YouTube
from sys import argv

weblink = argv[1]
yuTe = YouTube(weblink)

print("Title: ", yuTe.title)

print("View: ", yuTe.views)

yuTeDr = yuTe.streams.get_highest_resolution()

yuTeDr.download('/Users/Dark9ite/OneDrive/Desktop/dARK9ITE Store/Python/Python-Projects/youtube-downloader')