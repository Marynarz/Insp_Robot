from Tkinter import *

def GPS_mode():
    pass

def MANUAL_mode():
    pass

okno = Tk()
okno.title("INSP ROBOT")
okno.geometry("200x200")

lab1 = Label(okno,text="TRYB:")
but1 = Button(okno,text="GPS",command=GPS_mode)
but2 = Button(okno,text="MANUAL",command=MANUAL_mode)

lab1.pack()
but1.pack()
but2.pack()

okno.mainloop()