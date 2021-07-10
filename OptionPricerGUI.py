from numpy.lib.arraysetops import ediff1d
from yahoo_fin import stock_info 
from tkinter import *
import warnings
import numpy as np
import pandas_datareader.data as web
import pandas as pd
from math import log, exp, sqrt, pi
from scipy.stats import norm

#funcs
def stock_price(): 
    price = np.round(stock_info.get_live_price(e1.get()), 2)
    Current_stock.set(price)

def call_put_selector():
    choice = var.get()
    if choice == 1:
        #call
        print("call")
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
    r = float(risk_rate)
    v = float(vol)
    t = float(maturity)

    #call/put formulas
    d1 = (np.log(S/K) + (r + ((v*v)/2)) * t) / (v * sqrt(t))
    d2 = d1 - (v * sqrt(t))
    call = (norm.cdf(d1) * S) - (norm.cdf(d2) * K * exp(-r*t))
    put = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    call = np.round(call, 3)
    put = np.round(put, 3)
    call_res.set(call)
    put_res.set(put)

    n_prime_d1 = (exp(-(d1*d1)/2)) * (1/sqrt(2 * pi))
    #greeks

    #call
    call_delta = np.round(norm.cdf(d1), 4)
    call_gamma = np.round(n_prime_d1 / (S * v * sqrt(t)), 4)
    call_vega = np.round(S * sqrt(t) * n_prime_d1, 4)
    call_theta = np.round(-((S * n_prime_d1 * v) / (2 * sqrt(t))) - (r * K * exp(r*t) * norm.cdf(d2)), 4)
    call_rho = np.round(K * t * exp(r * t) * norm.cdf(d2), 4)

    #put
    put_delta = np.round(norm.cdf(d1) - 1, 4)
    put_gamma = np.round(n_prime_d1 / (S * v * sqrt(t)), 4)
    put_vega = np.round(S * sqrt(t) * n_prime_d1, 4)
    put_theta = np.round(-((S * n_prime_d1 * v) / (2 * sqrt(t))) + (r * K * exp(-r * t) * (1 - norm.cdf(d2))), 4)
    put_rho = np.round(-K * t* exp(-r * t) * (1 - norm.cdf(d2)), 4)

    delta_call.set(call_delta)
    gamma_call.set(call_gamma)
    vega_call.set(call_vega)
    theta_call.set(call_theta)
    rho_call.set(call_rho)

    delta_put.set(put_delta)
    gamma_put.set(put_gamma)
    vega_put.set(put_vega)
    theta_put.set(put_theta)
    rho_put.set(put_rho)


#GUI
master = Tk() 
master.geometry("600x400")
master.title("Black-Scholes Option Pricer")
Current_stock = StringVar()
call_res = StringVar()
put_res = StringVar()

#greeks
delta_call = StringVar()
gamma_call = StringVar()
vega_call = StringVar()
theta_call = StringVar()
rho_call = StringVar()

delta_put = StringVar()
gamma_put = StringVar()
vega_put = StringVar()
theta_put = StringVar()
rho_put = StringVar()


#define gui entries and labels
#var = IntVar()
#Label(master, text = "Option Type: ").grid(row = 0)
#Radiobutton(master, text = "Call", variable = var, value = 1).grid(row = 1, column = 1)
#Radiobutton(master, text = "Put", variable = var, value = 2).grid(row = 2, column = 1)

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

Label(master, text = "Call Option Price: ").grid(row = 13, column = 0, sticky = W)
call_result = Label(master, text="", textvariable=call_res).grid(row=13, column=1, sticky=W)
Label(master, text = "Put Option Price: ").grid(row = 13, column = 3, sticky = W)
put_result = Label(master, text = "", textvariable=put_res).grid(row=13, column = 4, sticky = W)

#greeks

#call greeks
Label(master, text = "Call Delta: ").grid(row = 16, column = 0, sticky = W)
Label(master, text = "Call Gamma: ").grid(row = 17, column = 0, sticky = W)
Label(master, text = "Call Vega: ").grid(row = 18, column = 0, sticky = W)
Label(master, text = "Call Theta: ").grid(row = 19, column = 0, sticky = W)
Label(master, text = "Call Rho: ").grid(row = 20, column = 0, sticky = W)

#call greek values
Label(master, text = "", textvariable = delta_call).grid(row = 16, column = 1, sticky = W)
Label(master, text = "", textvariable = gamma_call).grid(row = 17, column = 1, sticky = W)
Label(master, text = "", textvariable = vega_call).grid(row = 18, column = 1, sticky = W)
Label(master, text = "", textvariable = theta_call).grid(row = 19, column = 1, sticky = W)
Label(master, text = "", textvariable = rho_call).grid(row = 20, column = 1, sticky = W)

#put greeks
Label(master, text = "Put Delta: ").grid(row = 16, column = 3, sticky = W)
Label(master, text = "Put Gamma: ").grid(row = 17, column = 3, sticky = W)
Label(master, text = "Put Vega: ").grid(row = 18, column = 3, sticky = W)
Label(master, text = "Put Theta: ").grid(row = 19, column = 3, sticky = W)
Label(master, text = "Put Rho: ").grid(row = 20, column = 3, sticky = W)

#put greek values
Label(master, text = "", textvariable = delta_put).grid(row = 16, column = 4, sticky = W)
Label(master, text = "", textvariable = gamma_put).grid(row = 17, column = 4, sticky = W)
Label(master, text = "", textvariable = vega_put).grid(row = 18, column = 4, sticky = W)
Label(master, text = "", textvariable = theta_put).grid(row = 19, column = 4, sticky = W)
Label(master, text = "", textvariable = rho_put).grid(row = 20, column = 4, sticky = W)

mainloop()