from tkinter import *
screen = Tk()
screen.geometry("700x300")

def convert():
    celcius = celcius_entry.get()
    if celcius.replace(".", "", 1).isdigit():
        farenheit = (float(celcius) * 9/5) + 32
        farenheit_text.delete("1.0", END)
        farenheit_text.insert(END, farenheit)
    else:
        error_label.place(x = 270, y = 45)


celcius_label = Label(screen, text = "Enter The Temperature in Celcius:", font = ("Arial", 12))
celcius_label.place(x = 20, y = 20)

celcius_entry = Entry(screen)
celcius_entry.place(x = 270, y = 23)

convert_button = Button(screen, text = "Convert", font = ("Arial", 12), fg = "#5193e8", command = convert)
convert_button.place(x = 20, y = 50)

farenheit_label = Label(screen, text = "Farenheit", font = ("Arial", 12))
farenheit_label.place(x = 20, y = 180)
farenheit_text = Text(screen, width = 20, height = 1)
farenheit_text.place(x = 20, y = 220)

error_label = Label(screen, text = "Please enter valid input.", font = ("Consolas", 8), fg = "Red")

mainloop()