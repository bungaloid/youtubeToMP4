import tkinter
import os
import customtkinter
from pytube import YouTube

def startVideoDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        if video:
            title.configure(text=ytObject.title, text_color="white")
            finishlabel.configure(text="")            
            video.download()
            finishlabel.configure(text="Downloaded Video", text_color="white")
        else:
            finishlabel.configure(text="Download failed", text_color="red")
    except Exception as e:
        print("Exception:", e)
        finishlabel.configure(text="Download failed", text_color="red")

def startAudioDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(only_audio = True).first()

        if video:
            title.configure(text=ytObject.title, text_color="white")
            finishlabel.configure(text="")            
            out_file = video.download(output_path='.') 
  
            # save the file 
            base, ext = os.path.splitext(out_file) 
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
            finishlabel.configure(text="Downloaded Audio", text_color="white")
        else:
            finishlabel.configure(text="Download failed", text_color="red")
    except Exception as e:
        print("Exception:", e)
        finishlabel.configure(text="Download failed", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)



#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a Youtube link")
title.pack(padx = 10, pady = 10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 50, textvariable = url_var)
link.pack()

#Finished Downloading
finishlabel = customtkinter.CTkLabel(app, text = "")
finishlabel.pack()

#Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

#Download Video Button
downloadVideo = customtkinter.CTkButton(app, text = "Download Video", command = startVideoDownload)
downloadVideo.pack(padx=10,pady=10)

#Download Audio Button
downloadAudio = customtkinter.CTkButton(app, text = "Download Audio", command = startAudioDownload)
downloadAudio.pack(padx=10, pady=10)

#Run App
app.mainloop()