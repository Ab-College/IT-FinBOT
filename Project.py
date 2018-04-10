import csv
import requests
import webbrowser
import bs4
import tkinter as tk
from selenium import webdriver
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm
import quandl
import matplotlib.pyplot as plt
a=[]
symbol=""
txt=""
fa = ""
root = tk.Tk()
logo = tk.PhotoImage(file="axt.gif")
w1 = tk.Label(root, image=logo).pack(side="right")
explanation1 = """IT FinBOT : """
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10,font=('Arial',30),fg='blue',
              text=explanation1).pack(side="left")
explanation2 ="""Financial Analysis Application"""
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10,font=('Arial',20),fg='green',
              text=explanation2).pack(side="left")
root.mainloop()

f1 = open("secwiki_tickers.csv", "r")
reader = csv.reader(f1)
for row in reader:
        a.append(row)
#print(a)
fa=input('Enter the name of the company: ')
print('Entered Company: ' +fa)
for i in a:
        if i[1] == fa:
                symbol = i[0]
                break

print('Symbol of '+ fa + ' is : ' + symbol)

df=quandl.get("WIKI/"+symbol)
df = df[['Adj. Close']]
forecast_out = int(30) # predicting 30 days into future
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)
X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out]
y = np.array(df['Prediction'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)
 

clf = LinearRegression()
clf.fit(X_train,y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)

driver=webdriver.Firefox(executable_path=r'E:\Study\Python\geckodriver.exe')
driver.get('https://www.nasdaq.com/symbol/'+symbol+'/historical')
driver.close()
























    





        







