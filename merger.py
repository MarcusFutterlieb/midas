"""
Created on Tue Dec 03 2019
@author: Marcus Futterlieb
"""
# compare to CSV files on scraped from the web and one from the library
# TODO --> implement some kind of return that allows to check if merger has executed correctly
# TODO --> merger is broken --> the count of additional dates does not seem to work and dates in general are not merged


import csv;
import math;
import os;
from shutil import copyfile as cp;

def merger(stock):
    additionalDates = 0;
    internalErrorCode = 0;
    formatFactor = 2;
    dateStartPosition = 8;

    #create back up file in case this is the first time this particular stock is updated
    if not(os.path.exists('library/'+stock+'__backup.csv')):
        cp("library/"+stock+"__new.csv","library/"+stock+"__backup.csv");


    #get a row count of the scraped file to determine that the input format is correct
    with open('library/'+stock+'__new.csv', 'r') as t2:
        reader = csv.reader(t2, delimiter=",");
        data = list(reader);
        rowCount = len(data);
        # print(rowCount);
        if (rowCount != 32):
            print("Error: issue with rowcount");
    with open('library/'+stock+'__backup.csv', 'r') as t1, open('library/'+stock+'__new.csv', 'r') as t2, open(
            'library/'+stock+'__merge.csv', 'w') as merge:
        wr = csv.writer(merge, dialect='excel');
        for cnt in range(1, rowCount):
            #print(cnt);
            line_old = t1.readline();
            line_new = t2.readline();
            if (cnt % 2 != 0):  # write only the odd lines
                if (cnt <= (2 * formatFactor) - 1) or (cnt >= (12 * formatFactor) - 1):
                    #out of the bounds described in the if condition above, just copy paste information
                    wr.writerow([line_new.replace('"','')]);
            if (cnt == (3 * formatFactor) - 1):
                lastDateBackup = line_old[dateStartPosition:16];
                print ('line_old:  ',line_old)
                # lastDateBackup is the most recent date out of the merge file
                print('lastDateBackup: ',lastDateBackup, ' in stock: ', stock)
                # find the position of this date in the new file
                postionInNew = line_new.find(lastDateBackup, dateStartPosition-2);
                print('in the new string the most recent date that was also in backup was at position: ', postionInNew)
                #stringToParse.find(stringToFind,starting character)
                #print ('postionInNew:   ',postionInNew,'        ','dateStartPosition:  ',dateStartPosition)
                if (postionInNew != dateStartPosition):
                    #if the the most recent dates in new and backup file are not the same
                    if (postionInNew == -1):
                        #if it was note possible to find the most recent backup date in the new file (probably waited to long with the updating)
                        len(line_new);
                        newDateStr = line_new[0:len(line_new) - 2] + ',' + line_old[dateStartPosition:-1];
                        wr.writerow([newDateStr.replace('"','')]);
                        print('Could not find common date in files --> Has it been more than a month since you updated last?');
                        additionalDates = 0;
                        internalErrorCode = 1;
                    else:
                    #this should be the most popular use case --> most recent backup date is older than the most recent new date
                        # print (positionInNew);
                        # build the new string
                        newDateStr = line_new[0:postionInNew] + line_old[dateStartPosition:-1];
                        wr.writerow([newDateStr.replace('"','')]);
                        # print(newDateStr)
                        # determine how many new dates have been added
                        additionalDates = math.floor((postionInNew - dateStartPosition) / 12);
                        #print('additionalDates: ',additionalDates, ' in stock: ', stock)
                        #print('newDateStr',newDateStr,' in stock: ', stock, 'for the date row');
                else:
                #this should only be the case if its the first time the stock is being updated
                    print('Merger: This is the first time ', stock, ' is being updated')
                    #print('additionalDates:  ',additionalDates)
                    ##os.remove("library/" + stock + "__backup.csv");
                    #cp("library/" + stock + "__new.csv", "library/" + stock + "__merge.csv");
                    #cp("library/" + stock + "__new.csv", "library/" + stock + "__backup.csv");
                    #break; break;
                    newDateStr = line_new[0:-1];
                    wr.writerow([newDateStr.replace('"', '')]);
            elif (cnt == (4 * formatFactor) - 1):
                # should be the "open" key
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (5 * formatFactor) - 1):
                # should be the "high" key
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (6 * formatFactor) - 1):
                # should be the "low" key ##################
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1 - 1] + line_old[dateStartPosition - 1:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (7 * formatFactor) - 1):
                # should be the "close" key
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (8 * formatFactor) - 1):
                # should be the "tradeunits" key
                # find length of a element !!!Todo
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (9 * formatFactor) - 1):
                # should be the "volume" key
                # find length of a element !!!Todo
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (10 * formatFactor) - 1):
                # should be the "date" key
                # find last date for dividend that was equal in backup and new !!!Todo
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);
            elif (cnt == (11 * formatFactor) - 1):
                # should be the "dividend" key
                # possibly shift if there is a new dividend payment !!!Todo
                if (additionalDates != 0):
                    newDateStr = line_new[0:(additionalDates * 9) - 1] + line_old[dateStartPosition:-1];
                else:
                    newDateStr = line_new[0:-1];
                wr.writerow([newDateStr.replace('"','')]);


    if (internalErrorCode==0):
        os.remove("library/"+stock+"__backup.csv");
        cp("library/"+stock+"__merge.csv","library/"+stock+"__backup.csv");
    else:
        print("GUI:Merger:Internal Error");

            # print("Line {}: {}".format(cnt, line_old.strip()))
            #test = line_old.strip();
            # print('******');
            # print(test);
            # print('******');
    print('Found ', additionalDates , ' additionalDates while parsing library for stock: ' , stock) ;
    print('---------');
