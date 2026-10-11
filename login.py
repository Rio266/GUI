from tkinter import *
screen = Tk()
screen.geometry("450x450")
screen.title("Login Page")
screen.config(background = "blue")
username_label = Label(screen, text = "Username").place(x = 150, y = 100)
password_label = Label(screen, text = "Password").place(x = 150, y = 150)
username_entry = Entry(screen, width = 20).place(x = 250, y = 100)
password_entry = Entry(screen, width = 20, show = "*").place(x = 250, y = 150)

submit_button = Button(screen, text = "Submit", command = exit).place(x = 150, y = 250)
mainloop()