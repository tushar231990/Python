from tkinter import *
from pytube import YouTube

def Download():
    link = YouTube(yt_input.get())
    ys = link.streams.get_highest_resolution()
    ys.download(dl_loc_input.get())

def clear():
    yt_input.delete(0,END)
    dl_loc_input.delete(0,END)
    yt_input.focus_set()

root = Tk()

root.title("Youtube Downloader")
root.geometry("800x200")



yt_link=Label(root,text="Enter youtube link",fg="black",bg="grey",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
yt_input=Entry(root,width=50)
yt_input.grid(row=0,column=1,padx=10,pady=10)

dl_location=Label(root,text="Enter location to save video",fg="black",bg="grey",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)
dl_loc_input=Entry(root,width=50)
dl_loc_input.grid(row=1,column=1,padx=10,pady=10)

dl_btn = Button(root,command=Download,text="Download",fg="red",bg="white",font=("times new roman",15,"bold")).grid(row=2,column=1,padx=10,pady=10)
clear_btn = Button(root,command=clear,text="Clear",fg="red",bg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=10,pady=10)


root.mainloop()