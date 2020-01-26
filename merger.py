"""
Created on Tue Dec 03 2019
@author: Marcus Futterlieb
"""
# compare to CSV files on scraped from the web and one from the library
# TODO --> implement some kind of return that allows to check if merger has executed correctly
# TODO --> merger is broken --> the count of additional dates does not seem to work and dates in general are not merged
# TODO --> replace the rowcount with the function from little helper


import os;
from shutil import copyfile as cp;
import pandas;
from pandas import DataFrame


def merger(stock):
    lastDateOverlap = -99
    if not (os.path.exists('library/' + stock + '__hist__merge.csv')):
        # create the merge file in case this is the first time this particular stock is updated
        print('merger: file is being updated for the first time --> setting up merge files')
        cp("library/" + stock + "__hist__new.csv", "library/" + stock + "__hist__merge.csv");
        cp("library/" + stock + "__divi__new.csv", "library/" + stock + "__divi__merge.csv");
        cp("library/" + stock + "__perf__new.csv", "library/" + stock + "__perf__merge.csv");
    else:
        print('merger: there is an old file of this stock --> updating')
        historicValues_new = pandas.read_csv('./library/' + stock + '__hist__new.csv')
        historicValues_old = pandas.read_csv('./library/' + stock + '__hist__merge.csv')
        latestDate_new = historicValues_new['stockDates'].iloc[0]
        latestDate_old = historicValues_old['stockDates'].iloc[0]

        if (latestDate_new == latestDate_old):
            print('merger: update not necessary since the latest dates in both files are the same')
        else:
            print('merger: finding the position where merge and new had the same date')
            for cnt in range(1, historicValues_old['stockDates'].size):
                # print(cnt)
                # print(historicValues_new['stockDates'].iloc[cnt])
                if (historicValues_new['stockDates'].iloc[-1] == historicValues_old['stockDates'].iloc[cnt]):
                    lastDateOverlap = cnt
                    break
                else:
                    lastDateOverlap = -99
            historicValues_merge = 0
            if (lastDateOverlap == -99):
                print('merger: their are no overlapping dates in the stock s history file, appending all')
                # copy all of the new file on top of merger
                historicValues_merge = historicValues_new.append(historicValues_old)
            else:
                print('merger: a overlapping date was found, appending from: ',
                      historicValues_old['stockDates'].iloc[lastDateOverlap], ' at ', lastDateOverlap)
                historicValues_merge = historicValues_new.append(historicValues_old.iloc[lastDateOverlap + 1:-1])

            df1 = DataFrame(historicValues_merge,
                            columns=['stockDates', 'stockOpen', 'stockHigh', 'stockLow', 'stockClose',
                                     'stockTradedUnits', 'stockVolume'])
            export_csv1 = df1.to_csv(r'./library/' + stock + '__hist__merge.csv', index=None, header=True)
            print('merger: finished updating: ', stock, ' info')

    # remove uneccesary files
    os.remove('./library/' + stock + '__hist__new.csv')
    os.remove('./library/' + stock + '__divi__new.csv')
    os.remove('./library/' + stock + '__perf__new.csv')
    print('merger: removed unnecessrary files')

