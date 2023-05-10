from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os

global file_path

print("Launching...")
window = tk.Tk()
window.title("MP3Downloader")
window.minsize(200, 100)  # width, height
window.geometry("300x300+50+50")


label = tk.Label(window, text="Enter URL:")
label.pack()

ULR_entry = tk.Entry(window, width=200,justify="center")
ULR_entry.pack()

label = tk.Label(window, text="Enter PATH:")
label.pack()
PATH_entry = tk.Entry(window, width=200, justify="center")
PATH_entry.pack()

def SelectFolder():
    file_path = filedialog.askdirectory()
    PATH_entry.insert(0,file_path)

PATH_button = tk.Button(window, text="Select destination folder", command=SelectFolder)
PATH_button.pack()


def trydownload():
    url = ULR_entry.get()
    try:
        yt = YouTube(url)
    except:
        print('ERROR1')
    destination = PATH_entry.get()
    video = yt.streams.get_audio_only()
    try:    
        out_file = video.download(output_path=destination)
    except:
        print("ERROR2")
    print("Downloading:", yt.title)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title, " has been successfully downloaded.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

button_download = tk.Button(window, text="Download", command=trydownload)
button_download.pack()

window.mainloop()
