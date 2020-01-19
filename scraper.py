# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 2019
@author: Marcus Futterlieb
"""
from bs4 import BeautifulSoup as bs;
from writeDictToCSV import writeDictToCSV as wcsv;
import requests;
import os; #to have access to clear
import time; #for now just to send my code to sleep
import csv;
import unicodedata; 
###
os.system('cls')
###

historicPrices = { 'date': [],	'open': [], 'high': [], 'low':[], 'close': [],
                'tradedUnits':[], 'volume':[]};
historicDividend = {'date': [],'dividend': [], 'yield':[]};

historicPerformance = { 'date': [], 'euro': [], 'percent': []};


aStock = {'name': 'tmp', 'historicPrices': historicPrices,
        'historicDividend': historicDividend, 'historicPerformance': historicPerformance,
        'appropriatePrice': 0};


with open('links.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
#print(content[0]);

r = requests.get(content[0]).text
#print (r.text)
websiteAsText = bs(r,'lxml');
aStock['name'] = content[0].split("/",4)[3];
# take the first element of content and split it 4 times according to "/" then take the 4th element [3]
stockTable = websiteAsText.find('div',class_='abstand new');#use underscore because class is a keyword in python

stockTableName = stockTable.find('div',class_='arheadgl new');#use underscore because class is a keyword in python
stockTableName = stockTableName.h3.text;
##todo --> check if the content here is "Historische Kurse"

stockTableTable = stockTable.find('table',class_='line');
stockTableHeader = stockTableTable.find('tr',class_='subtitle')# you can also write it like this 'tr',{'class': 'subtitle'}
for td in stockTableHeader.find_all(['td',{'class': 'ql_hist_quote right'},'td',{'class': 'ql_date'}]):
    StockTableHeaderData = td.text;
    #print(StockTableHeaderData);
##check if the order of the data is still correct = tableheader
#print('end++++++++++++++++++++++++header');
################################################################historic values
loopCounter = 1;
for dataRows in stockTableTable.find_all(['tr',{'class': 'arrow0'}]):
    if loopCounter >1:#removing the header to not have it double int the library
        for data in dataRows.td:
            aStock['historicPrices']['date'].append(data);
        loopCounterNested=1;
        #print(dataRows.find_all(['td',{'class': 'font-size-14'}]))
        for data in dataRows.find_all(['td',{'class= font-size-14 right'}]):
            #print(unicodedata.normalize("NFKD", data.contents[0]));
            #print (loopCounterNested)
            if (loopCounterNested==2):
                aStock['historicPrices']['open'].append(data.contents[0].strip()); 
            elif (loopCounterNested==3):
                aStock['historicPrices']['high'].append(data.contents[0].strip());
            elif (loopCounterNested==4):
                aStock['historicPrices']['low'].append((data.contents[0]).strip());
#                print('---'+(unicodedata.normalize("NFKD", data.contents[0]))+'---')
#                print('---'+(data.contents[0])+'---')
#                print('---'+(data.contents[0]).strip()+'---')
#                print('-------------------------------------')
            elif (loopCounterNested==5):
                aStock['historicPrices']['close'].append(data.contents[0].strip());
            elif (loopCounterNested==7):
                aStock['historicPrices']['tradedUnits'].append(data.contents[0].strip());
            elif (loopCounterNested==8):
                aStock['historicPrices']['volume'].append(unicodedata.normalize("NFKD", data.contents[0]));
    #        else:
    #           print('do nothing');
            #print(loopCounterNested)
            #print(data2)
            
            loopCounterNested=loopCounterNested+1;
    loopCounter = loopCounter + 1;

################################################################historic dividend
loopCounter = 1;
dividendElement = websiteAsText.find('div',class_='histEventsBox abstand new');
dividendTable = dividendElement.find('table',class_='line');
for dataRows in dividendTable.find_all(['tr',{'class': 'arrow0'}]):
    #print(dataRows);
    loopCounterNested=1;
    for data in dataRows.find_all(['td',{'class='}]):
        #you can also try to remove the \t \n manually
        #result = data.replace('\n', '')
        #result = data.replace('\t', '')
        #print(data.get_text(strip=True))
        if(loopCounterNested==1):
            aStock['historicDividend']['date'].append(data.get_text(strip=True)); 
        elif(loopCounterNested==4):
            aStock['historicDividend']['dividend'].append(data.get_text(strip=True)); 
        #elif(loopCounterNested==3):
        #    aStock['historicDividend']['yield'].append(data.contents[0]); 
        loopCounterNested=loopCounterNested+1;
    #print(loopCounter);
    loopCounter = loopCounter + 1;

################################################################historic performance
loopCounter = 1;
performanceElement = websiteAsText.find('div',class_='histPerformance abstand new');
performanceTable = performanceElement.find('table',class_='line');
for dataRows in performanceTable.find_all(['tr',{'class': 'arrow0'}]):
    #print(dataRows);
    loopCounterNested=1;
    for data in dataRows.find_all(['td',{'class='}]):
        #you can also try to remove the \t \n manually
        #result = data.replace('\n', '')
        #result = data.replace('\t', '')
        #print(data.get_text(strip=True))
            
        if(loopCounterNested==1):  
            aStock['historicPerformance']['date'].append(data.get_text(strip=True)); 
        elif(loopCounterNested==2):
            aStock['historicPerformance']['euro'].append(unicodedata.normalize("NFKD", data.contents[0])); 
        elif(loopCounterNested==3):
            aStock['historicPerformance']['percent'].append(data.get_text(strip=True)); 
        #elif(loopCounterNested==3):
        #    aStock['historicDividend']['yield'].append(data.contents[0]); 
        loopCounterNested=loopCounterNested+1;
    #print(loopCounter);
    loopCounter = loopCounter + 1;

################################################################invoke saving function
wcsv(aStock['name'],aStock);
#print(aStock)
    
    #stockTableTableData = data.text;
    #print(stockTableTableData);
    #time.sleep(0.1)
#print('end+++++++++++++++++++++++data')


########update database csv file
##create
#this is where all the data should be

#print(stockTableName.prettify());
#print(stockTableContent.prettify());
#print(stockTableTable.prettify());
