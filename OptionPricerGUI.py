from yahoo_fin import stock_info 
from tkinter import *
import warnings
import numpy as np
import pandas_datareader.data as web
import pandas as pd

#funcs
def stock_price(): 
    price = stock_info.get_live_price(e1.get()) 
    Current_stock.set(price)

def call_put_selector():
    choice = var.get()
    if choice == 1:
        #call
        pass
    if choice == 2:
        #put
        pass

#GUI
master = Tk() 
master.geometry("600x400")
Current_stock = StringVar()
str_stock = StringVar()

#define option types
var = IntVar()
Label(master, text = "Option Type: ").grid(row = 0)
Radiobutton(master, text = "Call", variable = var, value = 1).grid(row = 1, column = 1)
Radiobutton(master, text = "Put", variable = var, value = 2).grid(row = 2, column = 1)

Label(master, text="Underlying : ").grid(row=3, sticky=W) 
Label(master, text="Spot:").grid(row=4, sticky=W) 
  
result2 = Label(master, text="", textvariable=Current_stock, 
                ).grid(row=4, column=1, sticky=W) 
  
e1 = Entry(master) 
e1.grid(row=3, column=1, sticky = W) 

b = Button(master, text="Show", command=stock_price) 
b.grid(row=3, column=2, columnspan=2, rowspan=2, padx=5, pady=5, sticky = W) 

mainloop()