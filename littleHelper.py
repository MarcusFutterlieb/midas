# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 2020

@author: Marcus Futterlieb
"""

import os;
import csv;
#from os.path import isfile, join
from pandas import DataFrame



def libraryParser(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#    for item in onlyfiles:
#        print(item);
    print(onlyfiles);



def rowCount(file):
    with open(file, 'r') as t2:
        reader = csv.reader(t2, delimiter=",")
        data = list(reader)
        rowCount = len(data)
        # print(rowCount);
        # print('rowcount OK');
        if (rowCount != 32):
            print("Error: issue with rowcount")
            return (999)
        else:
            return (rowCount)

def writeToCSV (stockName, stockDates, stockOpen,stockHigh ,stockLow, stockClose, stockTradedUnits, stockVolume,
                   stockDivDate, stockDivValue, stockDivYield, stockPerformanceDate,
                   stockPerformanceCurrency, stockPerformancePercent):
    #try to create the library archive
    try:
        os.mkdir("./library")
    except OSError as e:
       print("writeToCSV: Directory (./library) exists")


    bundledInformation1 = {'stockDates': stockDates, 'stockOpen': stockOpen, 'stockHigh': stockHigh,
                           'stockLow': stockLow,
                           'stockClose': stockClose, 'stockTradedUnits': stockTradedUnits, 'stockVolume': stockVolume}
    bundledInformation2 = {'stockDivDate': stockDivDate, 'stockDivValue': stockDivValue, 'stockDivYield': stockDivYield}
    bundledInformation3 = {'stockPerformanceDate': stockPerformanceDate,
                           'stockPerformanceCurrency': stockPerformanceCurrency,
                           'stockPerformancePercent': stockPerformancePercent}

    df1 = DataFrame(bundledInformation1, columns=['stockDates', 'stockOpen', 'stockHigh', 'stockLow', 'stockClose',
                                                  'stockTradedUnits', 'stockVolume'])
    df2 = DataFrame(bundledInformation2, columns=['stockDivDate', 'stockDivValue',
                                                  'stockDivYield'])
    df3 = DataFrame(bundledInformation3, columns=['stockPerformanceDate', 'stockPerformanceCurrency',
                                                  'stockPerformancePercent'])
    export_csv1 = df1.to_csv(r'./library/' + stockName + '__hist__new.csv', index=None, header=True)
    export_csv2 = df2.to_csv(r'./library/' + stockName + '__divi__new.csv', index=None, header=True)
    export_csv3 = df3.to_csv(r'./library/' + stockName + '__perf__new.csv', index=None, header=True)
    print ('writeToCSV: ', stockName, ' has been written into your personal library')
