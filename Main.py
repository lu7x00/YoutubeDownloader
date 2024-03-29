import os
from pytube import YouTube

folderName = ""


def show_progress_bar(stream, _chunk, _file_handle, bytes_remaining):
    current = stream.filesize - bytes_remaining
    status = int(current * 100 / stream.filesize)
    leftBracket = "["
    sharp = "#" * int(status / 10)
    blank = " " *  int(10 - status / 10)
    rightBracket = "]"
    progressBar = leftBracket + sharp + blank + rightBracket + " " + str(status) + "%"
    if status % 10 == 0:
        print("", end="\r")
        print(progressBar, end="")


URL = input("URL of video/audio on YouTube: ")
yt = YouTube(URL)
yt.register_on_progress_callback(show_progress_bar)
print("Searching...")
print(yt.title)

folderName = input("Enter name of folder with your audio/video: ")
os.mkdir(folderName)

print("(1) Audio\t(2) Video\t(3) Audio-Video\nOption:", end=" ")
choice = int(input())

if choice == 1:
    stream = yt.streams.get_by_itag('140')
    stream.download("./" + folderName)
elif choice == 2:
    print("Quality: \n(144) 144p\n(240) 240p\n(360) 360p\n(480) 480p\n(720) 720p\n(1080) 1080p")
    quality = int(input("Quality of Video: "))
    if quality == 144:
        stream = yt.streams.get_by_itag('160')
        stream.download("./" + folderName)
    if quality == 240:
        stream = yt.streams.get_by_itag('133')
        stream.download("./" + folderName)
    if quality == 360:
        stream = yt.streams.get_by_itag('134')
        stream.download("./" + folderName)
    if quality == 480:
        stream = yt.streams.get_by_itag('135')
        stream.download("./" + folderName)
    if quality == 720:
        stream = yt.streams.get_by_itag('136')
        stream.download("./" + folderName)
    if quality == 1080:
        stream = yt.streams.get_by_itag('137')
        stream.download("./" + folderName)
elif choice == 3:
    print("Quality: \n(360) 360p\n(720) 720p")
    print("Quality of audio/video: ", end="")
    quality = int(input())
    if quality == 360:
        stream = yt.streams.get_by_itag('18')
        stream.download("./" + folderName)
    if quality == 720:
        stream = yt.streams.get_by_itag('22')
        stream.download("./" + folderName)


input("\nDone. Press Enter to exit!")
