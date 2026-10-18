from tkinter import *
screen = Tk()
screen.geometry("300x300")
scroller = Scrollbar(screen)
scroller.pack(side = RIGHT, fill = Y)
listbox = Listbox(screen, yscrollcommand = scroller.set)
for i in range(50):
    listbox.insert(END, i)
listbox.pack(side = LEFT, fill = BOTH)
scroller.config(command = listbox.yview)
mainloop()