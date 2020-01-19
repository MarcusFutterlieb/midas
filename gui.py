# -*- coding: utf-8 -*-
"""
Created on Sun 19 Jan 2020
@author: Marcus Futterlieb
"""

#!/usr/bin/python

import os
import tkinter;
from tkinter import messagebox;

top = tkinter.Tk()
print("GUI started");

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")
   print("example function is executed");

B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()

def scraperCallBack():
   messagebox.showinfo( "Progress", "Updating")
   os.system('python scraper.py')
   print("executing scraper");

C = tkinter.Button(top, text ="Update", command = scraperCallBack)
C.pack()




print("GUI ready");
top.mainloop()
print("User closed GUI");
