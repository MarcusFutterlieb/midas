# -*- coding: utf-8 -*-
"""
Created on Sun 19 Jan 2020
@author: Marcus Futterlieb
"""

# !/usr/bin/python

import os
import tkinter
import matplotlib.pyplot as plt
# matplotlib.use("TkAgg");
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame
import pandas
# from matplotlib.figure import Figure;

from tkinter import messagebox
from tkinter import ttk

from scraper import scraper
from merger import merger
from littleHelper import rowCount
from littleHelper import overviewUpdate
#from table import McListBox


# set up the main window -->start
top = tkinter.Tk()
top.title("Meedas - Securities Tracking")
top.geometry("600x600")
# set up the main window -->stop
print("GUI: started")
# set up the main window -->stop
# set up available tabs -->start
tab_parent = ttk.Notebook(top)
tab_securities = ttk.Frame(tab_parent)
tab_options = ttk.Frame(tab_parent)
tab_overview = ttk.Frame(tab_parent)
tab_parent.add(tab_options, text="Options")
tab_parent.add(tab_overview, text="Overview")
tab_parent.add(tab_securities, text="Securities")
tab_parent.pack(expand=1, fill='both')
# set up available tabs -->stop



# adding figures and plots --> start
if (os.path.isdir("./library")):
    historicValues_new = pandas.read_csv('./library/' + 'bmw_vz-aktie' + '__hist__merge.csv')
    #dpi = dots per inch
    figure1 = plt.Figure(figsize=(20, 1), dpi=60)
    ax1 = figure1.add_subplot(111)
    ax1.plot(historicValues_new['stockDates'], historicValues_new['stockClose'], color='g')
    plot1 = FigureCanvasTkAgg(figure1, tab_securities)
    plot1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    ax1.legend()
    ax1.set_xlabel('Dates')
    ax1.set_title('bmw_vz-aktie')

    for label in ax1.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

# adding figures and plots --> stop

# set up buttons --> start
def scraperCallBack():
    print("GUI: executing scraper")
    stockList = scraper()
    print("GUI: executing merger")
    merger(stockList)
    print("GUI: executing overview update")
    overviewUpdate(stockList)
    print("GUI: Update request finished")
    messagebox.showinfo("Progress", "Update finished")

def helpCallBack():
    messagebox.showinfo("Help?", "Contact this guy at that address")
    print("GUI: help button is executed")

button_update = tkinter.Button(tab_options, text="Update", command=scraperCallBack)
button_update.grid(row=0, column=0, padx=15, pady=15)

button_help = tkinter.Button(tab_options, text="Help", command=helpCallBack)
button_help.grid(row=1, column=0, padx=15, pady=15)

closeButton = tkinter.Button(tab_options, text="Close", command=exit)
closeButton.grid(row=2, column=0, padx=15, pady=15)
# set up buttons --> stop

#set up the tab change handle -->start
def handle_tab_changed(event):
    selection = event.widget.select()
    tab = event.widget.tab(selection, "text")
    print("text:", tab)
    stockList = 'tbd'
    if (stockList != 0 and tab=="Overview"):
        print("testsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        listBox.insert("", "end", values=stockList)

tab_parent.bind("<<NotebookTabChanged>>", handle_tab_changed)
#set up the tab change handle -->stop

# set up the overview tab --> start
cols = ('Name', 'Price', 'Date')
listBox = ttk.Treeview(tab_overview, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

#for
#    listBox.insert("", "end", values=(i, name, score))


# set up the overview tab --> stop


print("GUI: ready")
top.mainloop()
print("User closed GUI")
