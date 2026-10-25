from tkinter import *
import calendar
screen = Tk()
screen.geometry("300x300")
text_label = Label(screen, text = "Calender", fg = "black", bg = "blue", font = ("Arial", 30)).place(x = 70, y = 20)
year_label = Label(screen, text = "Enter The Year", font = ("Arial", 12)).place(x = 20, y = 90)
year_entry = Entry(screen)
year_entry.place(x = 20, y = 120)
def task():
    screen_b = Tk()
    screen_b.geometry("600x600")
    year = int(year_entry.get())
    content = calendar.calendar(year)
    display_label = Label(screen_b, text = content)
    display_label.place(x = 0, y = 0)
submit_button = Button(screen, text = "Submit", command = task, font = ("Arial", 12)).place(x = 20, y = 180)
exit_button = Button(screen, text = "Exit", command = exit, font = ("Arial", 12)).place(x = 20, y = 220)
mainloop()