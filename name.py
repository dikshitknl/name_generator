import pandas as pd
from pandas import DataFrame, read_csv
import os,gender
import re,time
from random import randint
from Tkinter import *

loc = os.getcwd()

df = pd.read_csv(loc+r'\name_list.csv',names = ['Names', 'Gender', 'Meaning'])

def gui(title,ques):
    a = Tk()
    a.title(title,ques)
    a.geometry("450x300+200+200")

    labelText = StringVar()
    labelText.set(ques)
    label1 = Label(a,textvariable = labelText, height = 5).pack()

    message = IntVar()
    msg = Entry(a, textvariable = message)
    msg.pack()
    butn = Button(a,text = "Send",width = 18, command = check_gender).pack(side = 'bottom',padx =15,pady=15)
    a.mainloop()

def check_gender():
    dict_names = df['Names'].to_dict()
    tot = df['Names'].count()
    gui("Check_Gender","Input Name:")
    count = 0
    for i,j in dict_names.iteritems():
        if nam.capitalize() == j:
            gen = str(df['Gender'][i])
            count = i
            break
        else:
            gen = gender.check(nam)
    val = "Your Name :"+nam.capitalize()+"\nYou are a "+gen
    try:
        df['Meaning'][count]
    except KeyError:
        val += "Your Name meaning not found"
##        ch = raw_input("Are you satisfied with result? (Y or N)")
##        if ch.capitalize() == 'Y':
##            print "Can you please add the meaning of your name? (Y or N)"
##            ch1 = raw_input()
##            if ch1.capitalize() == 'Y':
##                df['Names'][tot+1] = nam.capitalize()
##                df['Gender'][tot+1] = gen
##                df['Meaning'][tot+1] = raw_input("Your Name Meaning:")
##                time.sleep(3)
##                val = val+"Thank You!!!"
    else:
        val = val+"Your Name means '"+df['Meaning'][count]
    tkMessageBox.showinfo('Your Details:',val)
def generate_name():
    gui('Generate_Names','Enter the initial Character:')
    list_name = []
    names = []
    for i in list(df['Names']):
        if re.search(r'\b'+ch.capitalize()+'\B',i):
            list_name.append(i)
        else:
            continue
    count = input("No.of names to generate:")
    for i in range(0,count):
        name = list_name[randint(0,len(list_name))]
        if i<len(list_name):
             val = val + name + ', '
        else:
            print "Sorry limited names"
            break
check_gender()
