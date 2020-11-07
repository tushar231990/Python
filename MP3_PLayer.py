from tkinter import *
import os
import pygame


class Musicplayer:

    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry('1020x300+200+200')
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg='grey',fg='white',bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)

        songtrack = Label(trackframe,textvariable=self.track,width=20,bg='grey',fg='White',font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        trackstatus = Label(trackframe,textvariable=self.status,bg='grey',fg='White',font=("times new roman",15,"bold")).grid(row=0,column=1,padx=10,pady=10)

        buttonframe = LabelFrame(self.root,text="Controls",bg='white',fg='blue',bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)

        playbtn = Button(buttonframe,command=self.play_song,text="Play",width=6,height=1,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        pausebnt = Button(buttonframe,command=self.pause_song,text="Pause",width=6,height=1,font=("times new roman",15,"bold")).grid(row=0,column=1,padx=10,pady=10)
        stopbnt = Button(buttonframe,command=self.stop_song,text="Stop",width=6,height=1,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=10)



        playlistframe=LabelFrame(self.root,text="Playlist",bg='white',fg='black',bd=5,relief=GROOVE)
        playlistframe.place(x=600,y=0,width=400,height=200)

        scrol_y=Scrollbar(playlistframe,orient=VERTICAL)

        self.playlist=Listbox(playlistframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,bg='silver',fg='black',bd=5,relief=GROOVE,font=("times new roman",15,"bold"))

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        os.chdir("C:\\Users\\ts285a\\Desktop\\Songs")
        songtracks=os.listdir()

        for track in songtracks:
            self.playlist.insert(END,track)

    def play_song(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stop_song(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pause_song(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()




root = Tk()
Musicplayer(root)
root.mainloop()