from calendar import month
import uuid
import tkinter as tk
from datetime import date, datetime
from tkinter import END, messagebox
# import mysql.connector
from dateutil import relativedelta
import json
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *

# con = mysql.connector.connect(host="localhost", user="root", password="",database="airpur")
# cursorObject = con.cursor()

def addSave(entrys):
    v1 = str(entrys["a1"].get())
    v2 = str(entrys["b1"].get())
    v3 = str(entrys["c1"].get())
    v4 = str(entrys["d1"].get())
    v5 = str(entrys["k1"].get())
    v6 = str(entrys["w1"].get())
    v7 = str(entrys["e1"].get())
    v8 = str(entrys["f1"].get())

    # convert string to date object
    start_date_c = datetime.strptime(v7, "%d-%m-%Y")
    end_date_c = datetime.strptime(v8, "%d-%m-%Y")

    # Get the relativedelta between two dates
    total_cone = relativedelta.relativedelta(end_date_c,start_date_c,)
    # print(total_cone.days)

    # convert string to date object

    cur_date = datetime.today().strftime("%d-%m-%Y")
    cur_date = datetime.strptime(cur_date,"%d-%m-%Y")
    
    date_depart = datetime.strptime(v6,"%d-%m-%Y")
    dur_conge = relativedelta.relativedelta(cur_date, date_depart)

    total_months = (dur_conge.years * 12) + dur_conge.months 



    total_months = calc_dur(total_months)
    # print(total_months)

    rest = total_months - total_cone.days
    # print(rest)
    

    try :
        
        with open('test.json' , "r") as f:
            data = json.load(f)

        index =  uuid.uuid4().hex

        # print(index)

        checkCIN , checkCNSS   = chekEmployee(str(v2),str(v1))

        print(checkCIN,checkCNSS)
        if checkCNSS == True :
            tk.messagebox.showinfo('error','CNSS deja exist')
        elif checkCIN == True :
            tk.messagebox.showinfo('error','CIN deja exist')
        elif total_cone == 0 :
            tk.messagebox.showinfo('error',"la date d'entre incorect")
        else :
            
            data["CNSS"][index] = str(v1)
            data["CIN"][index] = str(v2)
            data["Nomcomplet"][index] = str(v3)
            data["dateNaissance"][index] = str(v4)
            data["Qpro"][index] = str(v5)
            data["dateEntre"][index] = str(v6)
            data["dateredepart"][index] = str(v7)
            data["dateretour"][index] = str(v8)
            data["Njourpayee"][index] = str(total_cone.days)
            data["restedeconges"][index] = str(rest)
            data["totaldconges"][index] = str(total_months)
            tk.messagebox.showinfo('Return','INSERT succses full ')

            reset_form(entrys)

            with open("test.json", "w") as jsonFile:
                json.dump(data, jsonFile)

    except :
        tk.messagebox.warning('error','samething wrong') 
def chekEmployee(cin,cnss):
    with open('test.json' , "r") as f:
        data = json.load(f)

    test1 = False
    test2 = False
    if len(cin) == 0:
        test1 = True
    elif len(cnss) == 0:
        test2 = True
    else :
        for c in data["CIN"].values():
            if cin ==  c :
                test1 = True
                break

        for c in data["CNSS"].values():
            if cnss ==  c :
                test2 = True
                break
    
    return test1 , test2


def reset_form(entrys):
    entrys["a1"].delete(0,END)
    entrys["b1"].delete(0,END)
    entrys["c1"].delete(0,END)
    entrys["d1"].delete(0,END)
    entrys["k1"].delete(0,END)
    entrys["w1"].delete(0,END)
    entrys["e1"].delete(0,END)
    entrys["f1"].delete(0,END)


def updateSave(index,entrys):
    

    reset_form(entrys)

    with open('test.json' , "r") as f:
        data = json.load(f)
    
    entrys["a1"].insert(0,data["CNSS"][index])
    entrys["b1"].insert(0,data["CIN"][index])
    entrys["c1"].insert(0,data["Nomcomplet"][index])
    entrys["d1"].insert(0,data["dateNaissance"][index])
    entrys["k1"].insert(0,data["Qpro"][index])
    
    entrys["w1"].insert(0,data["dateEntre"][index])
    entrys["e1"].insert(0,data["dateredepart"][index])
    entrys["f1"].insert(0,data["dateretour"][index])
    entrys["g1"].insert(0,data["Njourpayee"][index])
    entrys["h1"].insert(0,data["restedeconges"][index])
    

    

def saveUpdate(index,entrys):

     
    

    # v1 = entrys["a1"].get()
    v3=entrys["c1"].get()
    v4=str(entrys["d1"].get_date())
    v5=entrys["k1"].get()
    v6=str(entrys["w1"].get_date())
    v7=str(entrys["e1"].get_date())
    v8=str(entrys["f1"].get_date())
    v9=entrys["g1"].get()
    v10=entrys["h1"].get()

    with open('test.json' , "r") as f:
        data = json.load(f)

    
    # data["CNSS"][index] = str(v1)
    # data["CIN"][index] = str(v2)
    data["Nomcomplet"][index] = str(v3)
    data["dateNaissance"][index] = str(v4)
    data["Qpro"][index] = str(v5)
    data["dateEntre"][index] = str(v6)
    data["dateredepart"][index] = str(v7)
    data["dateretour"][index] = str(v8)
    data["Njourpayee"][index] = str(v9)
    data["restedeconges"][index] = str(v10)
    # data["totaldconges"][index] = str(total_cone)
    tk.messagebox.showinfo('Return','update succses full ')

    with open("test.json", "w") as jsonFile:
        json.dump(data, jsonFile)



def calc_dur(months):
    if months >= 0 :
        if months <= 12:
            months = int(months * 1.5)
        elif months >12 and months<12*5:
            months = 18 
        elif months >=12*5 and months < 12*10 :
            months = 20
        elif months >=12*10 and months < 12*15 :
            months = 21
        elif months >=12*15 and months < 12*20 :
            months = 23
        elif months >=12*20 and months < 12*25 :
            months = 24
        elif months >= 12*25 :
            months = 25
        return months
    else :
        return 0

    