from tkinter import *
from tkvideo import tkvideo
w=Tk()
w.title("Video Player")
lblvideo=Label(w)
lblvideo.grid()
player=tkvideo("fgui.mp4", lblvideo, loop=1, size=(1530,789))#(1366,720)
player.play()
#Label1=lblvideo(player, text="kirtan")
#Label1.Pack()
#Label1.Place(x=0,y=0)
w.mainloop()
#print("kkirts")
