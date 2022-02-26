from cProfile import label
from importlib.resources import read_text
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("700x600")
root.title('YOUTUBE DOWNLOADER PROTO')
youtube_logo = PhotoImage(file='youtube.png')
root.iconphoto(True,youtube_logo)

frame=Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

background = PhotoImage(file='youtube.png')
backgroung_label = Label(frame, image=background)
backgroung_label.place(relx=0, relwidth=1.2, relheight=1.2)

Label(root,text='youtube downloader', bg='lightgreen', font=('Times', 30, 'bold')).place(x=10,y=50)
video_url = StringVar()
Label(root, text= 'place your link below', font=('Times', 25, 'bold')).place(x=10, y=110)
Entry(root, width=50, font= 35, textvariable=video_url, bd=5).place(x=90, y=170)

def videos():
    vides=YouTube(str(video_url.get()))
    downloader = vides.streams.get_highest_resolution()
    max_size = downloader.filesize
    print(max_size)
    downloader.download()
    Label(root, text= 'download completed', font= ('Times',25,'bold')).place(x=250,y=200)


Button(root, text= 'download',command=videos,font=('Times',25,'bold'), bg='lightgreen').place(x=200, y=220)
Button(root, text='quit',command=root.destroy, font=('Times', 25, 'bold')).place(x=450,y=220)
root.mainloop()