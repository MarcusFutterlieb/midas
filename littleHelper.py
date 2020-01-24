# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 2020

@author: Marcus Futterlieb
"""

import os;
#from os.path import isfile, join



def libraryParser(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))];
#    for item in onlyfiles:
#        print(item);
    print(onlyfiles);
