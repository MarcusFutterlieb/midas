# -*- coding: utf-8 -*-
"""
Created on Fri 20 Sep 2019
@author: Marcus Futterlieb
"""

import csv
import os

def writeDictToCSV(csv_file,dict_data):
##############################################################save the new data    
    #try to create the library archive
    try:
        os.mkdir("./library")
    except OSError as e:
       print("Directory exists")
    
    
    
    
    #csv_header = ['date',	'open', 'high', 'low', 'close','currency',
    #            'tradedUnits', 'volume','date','dividend',
    #            'yield','week', 'month', 'threeMonth',
    #                   'currentYear', 'year', 'threeYears', 'appropriatePrice'];
    
    try:
        with open('./library/'+ csv_file + "__new.csv", 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            #wr.writerow(csv_header)
            wr.writerow(['keyy', 'dataa'])
            for key in dict_data.keys():
#                if keys=='historicPrices':
                
                
                if isinstance(dict_data.get(key),dict):
                    #print('found a dict')
                    for innerKey in dict_data[key].keys():
                        #print('key : currently writing inner:  ',innerKey);
                        #print('value : currently writing inner:  ',dict_data[key][innerKey]);
#                        writer.writerow([dict_data[key]]);
                        wr.writerow([innerKey,dict_data[key][innerKey]])
                else:
                    #print('key : currently writing outer:  ',key);
                    #print('value : currently writing outer:  ',dict_data[key]);
#                    writer.writerow([key]);
                    wr.writerow([key,dict_data[key]])
#                    
    except IOError as err:
        errno, strerror = err.args
        print("I/O error({0}): {1}".format(errno, strerror))
    return            


#WriteDictToCSV(csv_file,csv_columns,dict_data)
