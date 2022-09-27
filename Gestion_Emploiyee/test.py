import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from functools import partial
import pandas as pd
import form
import json
import os , shutil
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *

def remove():
   
    selected = Trv.selection()
    id = str(selected[0])

    with open('test.json' , "r") as f:
        data = json.load(f)

    MsgBox = tk.messagebox.askquestion('Delete employee','Are you sure you want to delete '+data["Nomcomplet"][id],icon = 'warning')
    if MsgBox == 'yes' :
        Trv.delete(id)
        for ob in data.values():
            ob.pop(id)
        with open("test.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    else : 
        tk.messagebox.showinfo('Return','You will now return to the application screen')

def callback():
    pass

def search(E1):
    global Trv
    global TrvFrm
    

    entry = E1.get()


    with open('test.json' , "r") as f:
        data = json.load(f)

    id = -1
    
    for i , j in data["CIN"].items():
        i = str(i)
        if entry == data["CIN"][i] or entry == data["Nomcomplet"][i] :
            id = i
            break
    if id == -1 :
        tk.messagebox.showinfo('info','name or cin indefine :')
    else :
        for i in Trv.get_children():
            Trv.delete(i)

        Trv.insert('', END,iid=data["CIN"][id], values=(data["CNSS"][id], data["CIN"][id],data["Nomcomplet"][id],data["dateNaissance"][id],data["Qpro"][id],data["dateEntre"][id],data["dateredepart"][id],data["dateretour"][id],data["Njourpayee"][id],data["restedeconges"][id],data["totaldconges"][id],))
        TrvFrm.update()



def refresh(Trv,TrvFrm):
   
    with open('test.json' , "r") as f:
        data = json.load(f)
    


    for i , j in data["CIN"].items():
        i = str(i)
        Trv.insert('', END,iid=i, values=(data["CNSS"][i], data["CIN"][i],data["Nomcomplet"][i],data["dateNaissance"][i],data["Qpro"][i],data["dateEntre"][i],data["dateredepart"][i],data["dateretour"][i],data["Njourpayee"][i],data["restedeconges"][i],data["totaldconges"][i],))
    
    TrvFrm.update()

def window():
    global TrvFrm
    global f1
    global f2
    global Trv
    global E1

    TrvFrm  = Tk()
    TrvFrm.title('AIRPUR+')
    TrvFrm.iconbitmap("images/AIRPUR.ico")
    TrvFrm.geometry("1920x1080")

    f2 = ttk.Frame(TrvFrm, relief=SUNKEN,borderwidth=10)
    f1 = ttk.Frame(TrvFrm, relief=SUNKEN)
    Trv = ttk.Treeview(f1, height=20 , show='headings')
    
    
    f2.pack(fill=None, expand=False)
    
    f1.pack(fill=None, expand=False,side='bottom', padx=0, pady=0)
    f2.columnconfigure(0, weight=1)
    f2.columnconfigure(1, weight=3)
    

    L1 = Label(f2, text="Entre CIN :")
    L1.grid(column=0, row=0, sticky=tk.W,pady=20)
    L1.config(font=("arial", 20))
    E1 = Entry(f2, bd=2,font=("arial", 15))
    E1.grid(column=1, row=0, sticky=tk.W,ipadx=7,ipady=7,pady=8,columnspan=2)
    
    entry = partial(search,E1)
    but1 = ttk.Button(
        f2, 
        text="rechercher", 
        command=entry
    )
    but1.grid(column=3, row=0, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    but2 = ttk.Button(
        f2, 
        text="suprimer", 
        command=remove
    )
    but2.grid(column=0, row=1, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    
    but3 = ttk.Button(
        f2, 
        text="Refreash", 
        command=refreash
    )
    but3.grid(column=1, row=1, sticky=tk.W,ipadx=30,ipady=10,pady=20)

    but4 = ttk.Button(
        f2, 
        text="Ajouter", 
        command=setupFormulair
    )
    but4.grid(column=2, row=1, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    but5 = ttk.Button(
        f2, 
        text="modifier", 
        command=setupFormulairUpdate
    )
    but5.grid(column=3, row=1, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    but6 = ttk.Button(
        f2, 
        text="Exel", 
        command=Exel
    )
    but6.grid(column=4, row=1, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    but7 = ttk.Button(
        f2, 
        text="Déconnecter", 
        command=dec
    )
    but7.grid(column=4, row=0, sticky=tk.W,ipadx=30,ipady=10,pady=20)
    
    TrvFrm.state("zoomed")
    refreash()

    TrvFrm.mainloop()

def Exel():

    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    # print(desktop)
    df_json = pd.read_json("test.json")
    # print(os.getcwd())
    if os.path.exists("Airpur1.xlsx"):
        os.remove("Airpur1.xlsx")
    df_json.to_excel("Airpur1.xlsx")
    shutil.copy2(os.getcwd()+"\\"+"Airpur1.xlsx", desktop)
    tk.messagebox.showinfo('Return','Fill is done')
# Exel()
         
def dec():
    TrvFrm.destroy()
    


def refreash():
    global Trv
    global f1
    global TrvFrm
    global E1
    
    E1.delete(0,END)

    clearFrame()
    

    Trv = ttk.Treeview(f1, height=20 , show='headings')

    Trv['columns']=('Clm1', 'Clm2', 'Clm3','Clm4','Clm5','Clm6','Clm7','Clm8','Clm9','Clm10','Clm11')

    vsb = ttk.Scrollbar(f1, orient="vertical", command=Trv.yview)
    vsb.pack(side='right', fill='y')
    Trv.configure(yscrollcommand=vsb.set)

    Trv.column("Clm1",width=120)
    Trv.heading('Clm1', text='CNSS')
    
    Trv.column("Clm2",width=120)
    Trv.heading('Clm2', text='CIN')
    
    Trv.column("Clm3",width=120)
    Trv.heading('Clm3', text='Nom et Prénom')
    
    Trv.column("Clm4",width=120)
    Trv.heading('Clm4', text='Date de Naissance')
    
    Trv.column("Clm5",width=120)
    Trv.heading('Clm5', text='Qualification Professionnelle')
    
    Trv.column("Clm6",width=120)
    Trv.heading('Clm6', text="Date D'Entree En Service")
    
    Trv.column("Clm7",width=120)
    Trv.heading('Clm7', text='Date Depart de Conge')
    
    Trv.column("Clm8",width=120)
    Trv.heading('Clm8', text='Date Retour de Conge')
    
    Trv.column("Clm9",width=120)
    Trv.heading('Clm9', text='Nombre de jours payés')
    
    Trv.column("Clm10",width=120)
    Trv.heading('Clm10', text='Le Reste de Conges')
    
    Trv.column("Clm11",width=120)
    Trv.heading('Clm11', text='Total de conges')

    refresh(Trv,TrvFrm)

    Trv.pack(side=TOP, fill="both", expand=True) 

     

def clearFrame():
    global f1
    for widget in f1.winfo_children():
        widget.destroy()
    
    

def setupFormulair():
    global f1
    clearFrame()
    form.form(f1)

def setupFormulairUpdate():
    global Trv
    global f1
    try :
        selected = Trv.selection()
        print(selected)
        if len(selected[0])!=0 :
            id = selected[0]
            clearFrame()
            form.form1(f1,id)
    except :
        pass

def Ajouter():
    global f1
    setupFormulair()
    
    

    




