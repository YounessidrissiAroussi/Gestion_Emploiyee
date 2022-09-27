from tkinter import *
from tkinter import messagebox
import test as nW
import json
import calendar
# from babel.dates import format_date, parse_date, get_day_names, get_month_names
# from babel.numbers import *


def login():
    #import file json
    f = open('login.json', 'r+')
    content = json.load(f)
    #get value entry login and password
    login = entry0.get()
    password = entry1.get()
    # two loops for get value json
    check = False
    for c in content:
        for e in content['Entries']:
            if e['Login'] == login  and e['Password'] == password:
                check = True
    if check == True:
        window.destroy()
        nW.window()
    else:
        messagebox.showerror("Error", "login or password incorrect                                            ")
        entry0.delete(0,END)
        entry1.delete(0,END)
        entry0.focus()
        return False
window = Tk()
window.geometry("862x519")
window.configure(bg = "#3a7ff6")
window.iconbitmap("images/AIRPUR.ico")
window.title("AIRPUR+")
canvas = Canvas(
    window,
    bg = "#3a7ff6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    431, 0, 431+431, 0+519,
    fill = "#fcfcfc",
    outline = "")

img0 = PhotoImage(file = "images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 561, y = 328,
    width = 180,
    height = 55)

canvas.create_text(
    120.0, 140.5,
    text = "AIR PUR",
    fill = "#fcfcfc",
    font = ("ARIAL", int(30.0)))

canvas.create_text(
    560.0, 95.0,
    text = "Connexion.",
    fill = "#515486",
    font = ("Roboto-Bold", int(24.0)))


canvas.create_rectangle(
    40, 162, 40+60, 162+5,
    fill = "#fcfcfc",
    outline = "")

entry0_img = PhotoImage(file = "images/img_textBox0.png")
entry0_bg = canvas.create_image(
    650.5, 167.5,
    image = entry0_img)

entry0 = Entry(
    font=("arial 15"),
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry0.place(
    x = 490.0, y = 137,
    width = 321.0,
    height = 59)

entry1_img = PhotoImage(file = "images/img_textBox1.png")
entry1_bg = canvas.create_image(
    650.5, 248.5,
    image = entry1_img)

entry1 = Entry(
    font=("arial 15"),
    bd = 0,
    bg = "#f1f5ff",
    show="*",
    highlightthickness = 0)

entry1.place(
    x = 490.0, y = 218,
    width = 321.0,
    height = 59)

window.resizable(False, False)
window.mainloop()
