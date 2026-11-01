from tkinter import *
screen = Tk()
screen.geometry("700x300")

def convert():
    kg = float(kg_entry.get())
    g = float(kg * 1000)
    oz = float(kg * 35.274)
    lb = float(kg * 2.20462)
    grams_box.delete("1.0", END)
    grams_box.insert(END, g)
    lb_box.delete("1.0", END)
    lb_box.insert(END, lb)
    oz_box.delete("1.0", END)
    oz_box.insert(END, oz)

kg_label = Label(screen, text = "Enter the weight in kg:", font = ("Arial", 12))
kg_label.place(x = 50, y = 12)
kg_entry = Entry(screen)
kg_entry.place(x = 230, y = 14)

g_label = Label(screen, text = "Grams", font = ("Arial", 12))
g_label.place(x = 50, y = 180)
grams_box = Text(screen, width = 16, height = 1)
grams_box.place(x = 50, y = 210)

oz_label = Label(screen, text = "Ounces", font = ("Arial", 12))
oz_label.place(x = 300, y = 180)
oz_box = Text(screen, width = 16, height = 1)
oz_box.place(x = 300, y = 210)

lb_label = Label(screen, text = "Pounds", font = ("Arial", 12))
lb_label.place(x = 550, y = 180)
lb_box = Text(screen, width = 16, height = 1)
lb_box.place(x = 550, y = 210)

convert_button = Button(screen, text = "Convert", font = ("Arial", 12), fg = "#5193e8", command = convert)
convert_button.place(x = 50, y = 40)
mainloop()