from tkinter import *
from pytube import YouTube

# Initializing tkinter
root = Tk()
root.geometry("400x350")
root.title("Youtube Video Downloader")

# Definition of the download function
def download():
    try:
        dl.set("Dowloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video Downloaded successfully")
    except Exception as e:
        dl.set("Mistake")
        root.update()
        link.set("Enter correct link")

# Created the label to welcome user
Label(root, text="Welcome to Youtube downloader", font="Consolas 15 bold").pack()
dl = StringVar()
dl.set("Enter the link below")
Entry(root, textvariable=dl, width=10).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download", command=download).pack()
root.mainloop()

print("toto")
