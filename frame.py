from tkinter import *
screen = Tk()
screen.geometry("300x300")
top_frame = Frame(screen, bg = "green", width = 300, height = 150)
button_a = Button(top_frame, text = "Button A", bg = "blue")
button_b = Button(top_frame, text = "Button B", bg = "blue")
top_frame.pack_propagate(False)
top_frame.pack()

button_a.pack(side = LEFT)
button_b.pack(side = RIGHT)

mainloop()