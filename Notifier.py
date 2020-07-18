import datetime
import time
from tkinter import *
from CricketScore import matchScores

window=Tk()
window.wm_title("Live Cricket Scores")

lines = matchScores()

upLeft = Frame(window, borderwidth=2, relief="solid", bg = 'WHITE')
upLeft.grid(row = 0, column = 0)
upRight = Frame(window, borderwidth=2, relief="solid", bg = 'ORANGE')
upRight.grid(row = 0, column = 3)
bottomLeft = Frame(window, borderwidth=2, relief="solid", bg = 'GREEN')
bottomLeft.grid(row = 3, column = 0)
bottomRight = Frame(window, borderwidth=2, relief="solid", bg = 'YELLOW')
bottomRight.grid(row = 3, column = 3)

l1=Label(upLeft,text="Score 1", bg = 'WHITE')
l1.grid(row=0,column=0)

l5=Label(upLeft,text=lines[0],height=5,width=60, bg = 'WHITE')
l5.grid(row=2,column=0)

l2=Label(upRight,text="Score 2", bg = 'ORANGE')
l2.grid(row=0,column=4)

l6=Label(upRight,text=lines[1],height=5,width=60, bg = 'ORANGE')
l6.grid(row=2,column=4)

l3=Label(bottomLeft,text="Score 3", bg = 'GREEN')
l3.grid(row=3,column=0)

l7=Label(bottomLeft,text=lines[2],height=5,width=60, bg = 'GREEN')
l7.grid(row=5,column=0)

l4=Label(bottomRight,text="Score 4", bg = 'YELLOW')
l4.grid(row=3,column=3)

l8=Label(bottomRight,text=lines[3],height=5,width=60, bg = 'YELLOW')
l8.grid(row=5,column=3)

def clock():
    lines = matchScores()

    l5['text'] = lines[0]
    l6['text'] = lines[1]
    l7['text'] = lines[2]
    l8['text'] = lines[3]
    window.after(2000, clock)

clock()
window.geometry("860x213")
window.mainloop()