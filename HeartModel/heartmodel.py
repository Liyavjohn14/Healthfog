import pandas as pd
from joblib import load
import sys
from numpy import genfromtxt
import numpy as np
import warnings
warnings.simplefilter("ignore")

filename = sys.argv[1]

import csv
data = list(csv.reader(filename, delimiter=","))
filename.close()
print(data)
X1=data[0][0:13]
print(X1)
X2=data[0][1:2]
X2.extend(data[0][3:4])
X2.extend(data[0][3:4])
X2.extend(data[0][5:6])
X2.extend(data[0][13:17])
print(X2)
clf3 = load('heart.joblib')
clf4 = load('diab.joblib')
age = int(X1[0])
gender = int(X1[1])
chestpaintype = int(X1[2])
hypertension = int(X1[3])
cholestrol = int(X1[4])
fbs = int(X1[5])
rest_ecg = int(X1[6])
heart_rate = int(X1[7])
eia = int(X1[8])
st_Depr = float(X1[9])
slope = int(X1[10])
fluro = int(X1[11])
thal = int(X1[12])
st = int(X2[0])
insulin = int(X2[1])
bmi = int(X2[2])
dpf = int(X2[3])
preg = int(X2[4])

row = [[age, gender, chestpaintype, hypertension, cholestrol, fbs, rest_ecg, heart_rate, eia, st_Depr, slope, fluro, thal]]
print(row)
row2 = [[age, hypertension, fbs, st, insulin, bmi, dpf, preg ]]
a = clf3.predict(row)
b = clf4.predict(row2)
print(a)
print(b)
if(a==1 and b==1):
  content='11'
if(a==0 and b==0):
  content='00'
if(a==1 and b==0):
  content='10'
if(a==0 and b==1):
  content='01'
print(content)
file = open('output.txt','w')
file.write(content)
file.close()
