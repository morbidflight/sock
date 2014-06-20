import csv

temp = ''
codes = []
filename = raw_input('Enter a file name, with extension: ')

with open(filename, 'r') as myfile:
    row = myfile.read()
    temp = row.split(',')
    #print temp
    for item in temp: 
        if item not in codes:
            codes.append(item)
    print codes
