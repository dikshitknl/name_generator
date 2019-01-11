import pandas as pd
from pandas import DataFrame, read_csv
import os,gender
import re
from random import randint

loc = os.getcwd()

df = pd.read_csv(loc+r'\name_list.csv',names = ['Names', 'Gender', 'Meaning'])

lis_gender = list(df['Gender'])
lis_names = list(df['Names'])
lis_min = list(df['Meaning'])

def check_gender():
    mean = ' '
    nam = raw_input("\nInput Name you want from:")
    for i in lis_names:
        cap = nam.capitalize()
        if cap == i:
            gen = lis_gender[lis_names.index(cap)]
            mean = str(lis_min[lis_names.index(cap)])
            break
        else:
            gen = gender.check(nam)
    print 'Found!!!\nYou are',gen
    if len(mean)>2:
        print "Meaning of your Name is \"",mean,'"'
    else:
        print"Meaning Not found"
def generate_name(ch):
    list_name = []
    names = []
    for i in lis_names:
        if re.search(r'\b'+ch.capitalize()+'\B',i):
            list_name.append(i)
        else:
            continue
    count = input("No.of names to generate:")
    for i in range(0,count):
        name = list_name[randint(0,len(list_name))]
        if i<len(list_name):
            print name,',',
        else:
            print "Sorry limited names"
            break
generate_name(raw_input("Input initials you want to search:"))

