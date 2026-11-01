from tkinter import *
import calendar
screen = Tk()
screen.geometry("490x490")
year_label = Label(screen, text = "Year:", font = ("Arial", 12)).place(x = 20, y = 18)
year_entry = Entry(screen)
year_entry.place(x = 70, y = 23)

month_label = Label(screen, text = "Month:", font = ("Arial", 12)).place(x = 300, y = 18)
month_entry = Entry(screen)
month_entry.place(x = 360, y = 23)
def task():
    year = int(year_entry.get())
    month = int(month_entry.get())
    content = calendar.month(year, month)
    display_label = Label(screen, text = content, font = "Consolas")
    display_label.place(x = 140, y = 180)
submit_button = Button(screen, text = "Show The Month", command = task, bg = "#5193e8", fg = "#78390d", font = ("Arial", 12)).place(x = 20, y = 60)
exit_button = Button(screen, text = "Exit", command = exit, font = ("Arial", 12)).place(x = 444, y = 60)
mainloop()