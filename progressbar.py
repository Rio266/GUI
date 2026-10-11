from tkinter import *
from tkinter.ttk import *
import time
screen = Tk()
screen.geometry("100x100")
bar = Progressbar(screen, orient = HORIZONTAL, length = 50)
def update():
    bar["value"] = 20
    screen.update_idletasks()
    time.sleep(1)

    bar["value"] = 40
    screen.update_idletasks()
    time.sleep(1.4)

    bar["value"] = 70
    screen.update_idletasks()
    time.sleep(0.7)

    bar["value"] = 100
bar.place(x = 20, y = 20)
start = Button(screen, text = "Start", command = update)
start.place(x = 20, y = 70)
mainloop()