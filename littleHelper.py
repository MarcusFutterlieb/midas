# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 2020

@author: Marcus Futterlieb
"""

import os;
import csv;
#from os.path import isfile, join



def libraryParser(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))];
#    for item in onlyfiles:
#        print(item);
    print(onlyfiles);



def rowCount(file):
    with open(file, 'r') as t2:
        reader = csv.reader(t2, delimiter=",");
        data = list(reader);
        rowCount = len(data);
        # print(rowCount);
        # print('rowcount OK');
        if (rowCount != 32):
            print("Error: issue with rowcount");
            return (999);
        else:
            return (rowCount);
