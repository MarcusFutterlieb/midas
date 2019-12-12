"""
Created on Tue Dec 03 2019

@author: Marcus Futterlieb
"""
# compare to CSV files on scraped from the web and one from the library


import csv;
import math;

with open('persons.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


formatFactor=2;
dateStartPosition = 8;
with open('library/bmw_vz-aktie__new.csv', 'r') as t2:
    reader = csv.reader(t2,delimiter = ",");
    data = list(reader);
    rowCount = len(data);
    #print(rowCount);
    if (rowCount!=32):
        print("Error: issue with rowcount");
with open('library/bmw_vz-aktie__backup.csv', 'r') as t1, open('library/bmw_vz-aktie__new.csv', 'r') as t2, open('library/bmw_vz-aktie__merge.csv', 'w') as merge:        
    wr = csv.writer(merge, dialect='excel');
    for cnt in range(1,rowCount):
        #print(cnt);
        line_old = t1.readline();
        line_new = t2.readline();
        if (cnt%2!=0):#write only the odd lines
            if(cnt<=(2*formatFactor)-1) or (cnt>=(12*formatFactor)-1):
                wr.writerow([line_new]);
        if (cnt==(3*formatFactor)-1):
            lastDateBackup = line_old[dateStartPosition:16];
            #print(lastDateBackup)
            #find the postion of this date in the new file
            postionInNew = line_new.find(lastDateBackup,dateStartPosition-1);
            if(postionInNew!=dateStartPosition):
                if (postionInNew==-1):
                    len(line_new);
                    newDateStr = line_new[0:len(line_new)-2] + ','+ line_old[dateStartPosition:-1];
                    wr.writerow([newDateStr]);
                    print('Could not find common date in files --> Has it been more than a month since you updated last?');
                else:
                    #print (postionInNew);
                    #build the new string
                    newDateStr = line_new[0:postionInNew] + line_old[dateStartPosition:-1];
                    wr.writerow([newDateStr]);
                    #print(newDateStr)
                    #determine how many new dates have been added 
                    additionalDates = math.floor((postionInNew - dateStartPosition)/12);
                    #print(additionalDates);
        elif (cnt==(4*formatFactor)-1):    
            #should be the "open" key
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(5*formatFactor)-1):    
            #should be the "high" key
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(6*formatFactor)-1):    
            #should be the "low" key ##################
            newDateStr = line_new[0:(additionalDates*9)-1-1] + line_old[dateStartPosition-1:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(7*formatFactor)-1):    
            #should be the "close" key
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(8*formatFactor)-1):    
            #should be the "tradeunits" key
            # find length of a element !!!Todo
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(9*formatFactor)-1):    
            #should be the "volume" key
            # find length of a element !!!Todo
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(10*formatFactor)-1):    
            #should be the "date" key
            # find last date for dividend that was equal in backup and new !!!Todo
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
        elif (cnt==(11*formatFactor)-1):    
            #should be the "dividend" key
            # possibly shift if there is a new dividend payment !!!Todo
            newDateStr = line_new[0:(additionalDates*9)-1] + line_old[dateStartPosition:-1];
            wr.writerow([newDateStr]);
            
            
            
           #print("Line {}: {}".format(cnt, line_old.strip()))
        test = line_old.strip();
        #print('******');
        #print(test);
        #print('******');
       
print('---------');

