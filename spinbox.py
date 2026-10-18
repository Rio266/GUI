from tkinter import *

screen = Tk()
screen.geometry("300x300")
spinbox = Spinbox(screen, from_ = 0, to = 9)
spinbox.place(x=20, y=0)
mainloop()