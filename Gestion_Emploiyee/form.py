from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from functools import partial
from function import addSave , updateSave ,saveUpdate
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *

def form(window):
    a = Label(window ,text = "CNSS")
    a.grid(row = 0,column = 0,padx=50,pady=30)
    b = Label(window ,text = "CIN")
    b.grid(row = 1,column = 0,padx=50,pady=30)
    c = Label(window ,text = "Nom et Prénom")
    c.grid(row = 2,column = 0,padx=50,pady=30)
    k = Label(window ,text = "Date de Naissance")
    k.grid(row = 3,column = 0,padx=50,pady=30)
    d = Label(window ,text = "Qualification Professionnelle")
    d.grid(row = 4,column = 0,padx=50,pady=40)
    # --------------------------------------------------------------
    e = Label(window ,text = "Date D'Entree En Service")
    e.grid(row = 0,column = 2,padx=50,pady=30)
    f = Label(window ,text = "Date Depart de Conge")
    f.grid(row = 1,column = 2,padx=50,pady=30)
    g = Label(window ,text = "Date Retour de Conge")
    g.grid(row = 2,column =2,padx=50,pady=30)
    h = Label(window ,text = "Nombre de jours payés")
    h.grid(row = 3,column = 2,padx=50,pady=30)
    w = Label(window ,text = "Le Reste de Conges")
    w.grid(row = 4,column = 2,padx=50,pady=40)
    # ---------------------------------------------------
    a1 = Entry(window)
    a1.grid(row = 0,column = 1,ipadx=30)
    b1 = Entry(window)
    b1.grid(row = 1,column = 1,ipadx=30)
    c1 = Entry(window)
    c1.grid(row = 2,column = 1,ipadx=30)
    d1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    d1.grid(row = 3,column = 1,ipadx=30)
    d1.delete(0, END)
    k1 = Entry(window)
    k1.grid(row = 4,column = 1,ipadx=30)

    w1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    w1.grid(row = 0,column = 3,ipadx=50)
    e1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    e1.grid(row = 1,column = 3,ipadx=50)
    f1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    f1.grid(row = 2,column = 3,ipadx=50)
    g1=  Entry(window)
    g1.grid(row = 3,column = 3,ipadx=30)
    g1.config(state= "disabled")
    h1=  Entry(window)
    h1.grid(row = 4,column = 3,ipadx=30)
    h1.config(state= "disabled")

    entrys = {
        "a1" : a1,
        "b1" : b1,
        "c1" : c1,
        "d1" : d1,
        "k1" : k1,
        "w1" : w1,
        "e1" : e1,
        "f1" : f1,
        "g1" : g1,
        "h1" : h1
    }
    save = partial(addSave,entrys)
    ajout = ttk.Button(
            window, 
            text="save", 
            command=save
        )
    ajout.grid(row = 5,column = 2,ipadx=30,ipady=10,pady=20)
    res = partial(form ,window)
    res = ttk.Button(
            window, 
            text="reset", 
            command=res
        )
    res.grid(row = 5,column = 3,ipadx=30,ipady=10,pady=20)

def form1(window , id):
    a = Label(window ,text = "CNSS")
    a.grid(row = 0,column = 0,padx=50,pady=30)
    b = Label(window ,text = "CIN")
    b.grid(row = 1,column = 0,padx=50,pady=30)
    c = Label(window ,text = "Nom et Prénom")
    c.grid(row = 2,column = 0,padx=50,pady=30)
    k = Label(window ,text = "Date de Naissance")
    k.grid(row = 3,column = 0,padx=50,pady=30)
    d = Label(window ,text = "Qualification Professionnelle")
    d.grid(row = 4,column = 0,padx=50,pady=40)
    # --------------------------------------------------------------
    e = Label(window ,text = "Date D'Entree En Service")
    e.grid(row = 0,column = 2,padx=50,pady=30)
    f = Label(window ,text = "Date Depart de Conge")
    f.grid(row = 1,column = 2,padx=50,pady=30)
    g = Label(window ,text = "Date Retour de Conge")
    g.grid(row = 2,column =2,padx=50,pady=30)
    h = Label(window ,text = "Nombre de jours payés")
    h.grid(row = 3,column = 2,padx=50,pady=30)
    w = Label(window ,text = "Le Reste de Conges")
    w.grid(row = 4,column = 2,padx=50,pady=40)
    # ---------------------------------------------------
    a1 = Entry(window)
    a1.grid(row = 0,column = 1,ipadx=30)
    b1 = Entry(window)
    b1.grid(row = 1,column = 1,ipadx=30)
    c1 = Entry(window)
    c1.grid(row = 2,column = 1,ipadx=30)
    d1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    d1.grid(row = 3,column = 1,ipadx=30)
    
    k1 = Entry(window)
    k1.grid(row = 4,column = 1,ipadx=30)

    w1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    w1.grid(row = 0,column = 3,ipadx=50)
    e1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    e1.grid(row = 1,column = 3,ipadx=50)
    f1 = DateEntry(window,date_pattern='dd-mm-yyyy')
    f1.grid(row = 2,column = 3,ipadx=50)
    g1=  Entry(window)
    g1.grid(row = 3,column = 3,ipadx=30)
    h1=  Entry(window)
    h1.grid(row = 4,column = 3,ipadx=30)

    entrys = {
        "a1" : a1,
        "b1" : b1,
        "c1" : c1,
        "d1" : d1,
        "k1" : k1,
        "w1" : w1,
        "e1" : e1,
        "f1" : f1,
        "g1" : g1,
        "h1" : h1
    }

    

    
    save = partial(saveUpdate,id,entrys)

    ajout = ttk.Button(
            window, 
            text="save", 
            command=save
        )
    ajout.grid(row=5,column=3,ipadx=30,ipady=10,pady=20)
    updateSave(id,entrys)

