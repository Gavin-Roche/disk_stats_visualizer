#four imports
import statistics
import csv
import numpy as np 
import matplotlib.pyplot as plt

#gets unit of measurment MB GB TB
def getDriveUOM(driveStr):
    return str(driveStr[-2:])
#gets the year 2 digets only, for the year row
def getYear(yearStr):
    return int(yearStr[-2:])
#gets the number only for the capacity
def measurmentOnly(capacityNumber):
    return float(capacityNumber[:-3])
 
#defines Lists
yearsList  = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
avgssdList = []
avghddList = []
minhddList = []
maxhddList = []
maxssdList = []
minssdList = []
#iterates through currentYear
for currentYear in range(8,20):
    #defines ssdList and hddList
    ssdList     = []
    hddList     = []
    
    #opens dataframes and skips headers
    with open ("Data.csv") as csv_file:
        dataFrame = csv.reader(csv_file, delimiter = ",")
        next(dataFrame)
        for row in dataFrame:
            #checks row to see if it matches currentYear and is ssd
            if getYear(row[5]) == currentYear:
                if (row[6]) == "SSD":
                    #gets tebibyte and converts to bytes and appends to ssdList
                    if getDriveUOM(row[1]) == "TB":
                        tibConverted = measurmentOnly(row[1]) * 1099511627776
                        ssdList.append(tibConverted)
                    #gets gibibyte and converts to bytes and appends to ssdList
                    elif getDriveUOM(row[1]) == "GB":
                        gibConverted = measurmentOnly(row[1]) * 1073741824
                        ssdList.append(gibConverted)
                    #gets mebibyte and converts to bytes and appends to ssdList
                    else:
                        mibConverted = measurmentOnly(row[1]) * 1048576
                        ssdList.append(mibConverted)
                #checks row to see if it is a hdd
                elif (row[6]) == "HDD":
                    #gets tebibyte and converts to bytes and appends to hddList
                    if getDriveUOM(row[1]) == "TB":
                        tibConverted = measurmentOnly(row[1]) * 1099511627776
                        hddList.append(tibConverted)
                    #gets gibibyte and converts to bytes and appends to hddList
                    elif getDriveUOM(row[1]) == "GB":
                        gibConverted = measurmentOnly(row[1]) * 1073741824
                        hddList.append(gibConverted)
                    #gets mebibyte and Converts to bytes and appends to hddList
                    else:
                        mibConverted = measurmentOnly(row[1]) * 1048576
                        hddList.append(mibConverted)
              
        #mean ssdAverage turn to gb and add to list
        ssdAverage = statistics.mean(ssdList) / 1000000000
        avgssdList.append(ssdAverage)

        #mean hddAverage turn to gb and add to list
        hddAverage = statistics.mean(hddList) / 1000000000
        avghddList.append(hddAverage)
        
        #ssdmin
        ssdmin = min(ssdList) / 1000000000
        minssdList.append(ssdmin)
        
        #ssdmax
        ssdmax = max(ssdList) / 1000000000
        maxssdList.append(ssdmax)
        
        #hddmin
        hddmin = min(hddList) / 1000000000
        minhddList.append(hddmin)
        
        #hddmax
        hddmax = max(hddList) / 1000000000
        maxhddList.append(hddmax)

# Define Data for graph
year = yearsList
ssd  = avgssdList
hdd  = avghddList

x_axis = np.arange(len(year))

# Multi bar Chart
plt.bar(x_axis -0.2, ssd, width=0.4, label = "ssd")
plt.bar(x_axis +0.2, hdd, width=0.4, label = "hdd")

# Xticks
plt.xticks(x_axis, year)

#labels y axis
plt.ylabel("GB")

# Add legend
plt.legend()

# Display
plt.show()