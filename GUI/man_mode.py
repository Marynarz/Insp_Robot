from Tkinter import *

def GPS_mode():
    pass

def MANUAL_mode():
    pass

okno = Tk()
okno.title("INSP ROBOT - MANUAL MODE")
okno.geometry("200x200")

#podstawowe widgety
frame1 = LabelFrame(okno,bd=2,text="control")
but1 = Button(okno,text="^")
but2 = Button(okno,text="<")
but3 = Button(okno,text=">")
but4 = Button(okno,text="\/")

#ulozenie widgetow
frame1.grid(row=0,column=4,rowspan=3)
but1.grid(row=1,column=1)
but2.grid(row=1,column=0,rowspan=2)
but3.grid(row=1,column=3,rowspan=2)
but4.grid(row=2,column=1)

okno.mainloop()