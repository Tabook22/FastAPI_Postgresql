import pytube
path="files/"
url=input("YoutTube url")
pytube.YouTube(url).streams.get_highest_resolution().download(path)