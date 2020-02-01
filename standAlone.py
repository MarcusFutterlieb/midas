# -*- coding: utf-8 -*-
"""
Created on Sun 01 Feb 2020
@author: Marcus Futterlieb
"""
from scraper import scraper
from merger import merger
from littleHelper import overviewUpdate

print("standAlone: executing scraper")
stockList = scraper()
print("standAlone: executing merger")
merger(stockList)
print("standAlone: executing overview update")
overviewUpdate(stockList)
print("standAlone: Update request finished")
