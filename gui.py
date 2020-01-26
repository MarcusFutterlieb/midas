# -*- coding: utf-8 -*-
"""
Created on Sun 19 Jan 2020
@author: Marcus Futterlieb
"""

# !/usr/bin/python

import os
import tkinter;
import matplotlib.pyplot as plt;
# matplotlib.use("TkAgg");
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg;
from matplotlib.figure import Figure
from pandas import DataFrame;
import pandas
# from matplotlib.figure import Figure;

from tkinter import messagebox;
from tkinter import ttk;

from scraper import scraper;
from merger import merger;
from littleHelper import rowCount;

# set up the main window -->start
top = tkinter.Tk();
top.title("Meedas - Securities Tracking");
top.geometry("600x600");
# set up the main window -->stop
print("GUI: started");

# set up available tabs -->start
tab_parent = ttk.Notebook(top);
tab_securities = ttk.Frame(tab_parent);
tab_options = ttk.Frame(tab_parent);
tab_overview = ttk.Frame(tab_parent);
tab_parent.add(tab_options, text="Options");
tab_parent.add(tab_overview, text="Overview");
tab_parent.add(tab_securities, text="Securities");
tab_parent.pack(expand=1, fill='both');
# set up available tabs -->stop


# adding figures and plots --> start
if (os.path.isdir("./library")):
    historicValues_new = pandas.read_csv('./library/' + 'bmw_vz-aktie' + '__hist__merge.csv')
    figure3 = plt.Figure(figsize=(5, 4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(historicValues_new['stockDates'], historicValues_new['stockClose'], color='g')
    scatter3 = FigureCanvasTkAgg(figure3, tab_securities)
    scatter3.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    ax3.legend()
    ax3.set_xlabel('Dates')
    ax3.set_title('bmw_vz-aktie')

# adding figures and plots --> stop

# set up buttons --> start
def scraperCallBack():
    messagebox.showinfo("Progress", "There should be a progress bar here")
    #os.system('python scraper.py');
    print("GUI: executing scraper")
    stockList = scraper()
    #print(stockList)
    #os.system('python merger.py')
    print("GUI: executing merger")
    merger(stockList)
    print("GUI: Update request finished")



button_update = tkinter.Button(tab_options, text="Update", command=scraperCallBack)
button_update.grid(row=0, column=0, padx=15, pady=15)


def helpCallBack():
    messagebox.showinfo("Help?", "Contact this guy at that address")
    print("GUI: help button is executed")


button_help = tkinter.Button(tab_options, text="Help", command=helpCallBack)
button_help.grid(row=0, column=1, padx=15, pady=15)
# set up buttons --> stop


print("GUI: ready");
top.mainloop()
print("User closed GUI")
