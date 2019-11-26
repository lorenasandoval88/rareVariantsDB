# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv

os.getcwd()
os.listdir()
os.chdir('C:/Users/sandovall2/Documents/GitHub/rareVariantsDB/csvfiles')
os.listdir()
with open("omim.csv") as csvfile:
    readCSV= csv.reader(csvfile)
    for number, line in enumerate(readCSV):
        if number < 5:
            print(line)
        else:
            break