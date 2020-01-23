import csv;

def rowCount(file):
    with open(file, 'r') as t2:
        reader = csv.reader(t2, delimiter=",");
        data = list(reader);
        rowCount = len(data);
        #print(rowCount);
        #print('rowcount OK');
        if (rowCount != 32):
            print("Error: issue with rowcount");
            return (999);
        else:
            return (rowCount);
