from numpy.lib.arraysetops import ediff1d
from yahoo_fin import stock_info 
from tkinter import *
import warnings
import numpy as np
import pandas_datareader.data as web
import pandas as pd
from math import log, exp, sqrt
from scipy.stats import norm

#funcs
def stock_price(): 
    price = np.round(stock_info.get_live_price(e1.get()), 2)
    Current_stock.set(price)

def call_put_selector():
    choice = var.get()
    if choice == 1:
        #call
        pass
    if choice == 2:
        #put
        pass

#function can be used to bind multiple commands to single entity.
def combine_funcs(*funcs):
    def inner_combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return inner_combined_func()

def get_selection():
    spot = e_0.get()
    strike = e_1.get()
    maturity = e_2.get()
    risk_rate = e_3.get()
    vol = e_4.get()

    #call option price
    S = int(spot)
    K = int(strike)
    r = int(risk_rate)
    v = int(vol)
    t = int(maturity)

    #call/put formulas
    d1 = (np.log(S/K) + (r + ((v*v)/2)) * t) / (v * sqrt(t))
    d2 = d1 - (v * sqrt(t))
    call = (norm.cdf(d1) * S) - (norm.cdf(d2) * K * exp(-r*t))
    put = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    print(call)
    print(put)


#GUI
master = Tk() 
master.geometry("600x400")
Current_stock = StringVar()

#define gui entries and labels
var = IntVar()
Label(master, text = "Option Type: ").grid(row = 0)
Radiobutton(master, text = "Call", variable = var, value = 1).grid(row = 1, column = 1)
Radiobutton(master, text = "Put", variable = var, value = 2).grid(row = 2, column = 1)

Label(master, text="Underlying : ").grid(row=3, sticky=W) 
Label(master, text="Spot:").grid(row=4, sticky=W) 
  
result2 = Label(master, text="", textvariable=Current_stock, 
                ).grid(row=4, column=1, sticky=W) 

 #underlying price 
e1 = Entry(master) 
e1.grid(row=3, column=1, sticky = W) 

b = Button(master, text="Show", command=stock_price) 
b.grid(row=3, column=3, columnspan=2, sticky = W)

'Black-Scholes Option Pricer Entries'
Label(master, text = "Parameters").grid(row = 5, sticky = W)

#spot price
Label(master, text = "Spot: ").grid(row = 6, sticky = W)
e_0 = Entry(master)
e_0.grid(row = 6, column = 1, sticky = W)

#strike price
Label(master, text = "Strike: ").grid(row = 7, sticky = W)
e_1 = Entry(master)
e_1.grid(row = 7, column = 1, sticky = W)

#time to maturity
Label(master, text = "Time to Maturity: ").grid(row = 8, sticky = W)
e_2 = Entry(master)
e_2.grid(row = 8, column = 1, sticky = W)

#risk-free interest rate
Label(master, text = "Risk-Free Interest Rate: ").grid(row = 9, sticky = W)
e_3 = Entry(master)
e_3.grid(row = 9, column = 1, sticky = W)

Label(master, text = "Implied Volatility: ").grid(row = 10, sticky = W)
e_4 = Entry(master)
e_4.grid(row = 10, column = 1, sticky = W)

b = Button(master, text = "Calculate", command=get_selection)
b.grid(row = 12, column = 1, sticky = W)

mainloop()