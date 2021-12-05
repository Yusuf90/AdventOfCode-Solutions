import sys
import os
import math
import pandas as pd

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day3')

def findRate(df_reports, searchForMost, currentBit):
    #searchForMost parameter is a boolean where true is Most(Oxygen) and false is Least(CO2 Scrubber)

    #base case: Stop if only 1 row is in dataframe
    if(len(df_reports.index) == 1):
        return df_reports.values.tolist()[0]
    #general case: Return a new dataframe with selected rows that start with '1' on the selected bit.
    else:
        #Take most common value if searchForMost (Oxygen), else take least common value (CO2 Scrubber)        
        search_criteria = df_reports[currentBit].value_counts().idxmax() if searchForMost else df_reports[currentBit].value_counts().idxmin()

        #if both values occur equally amount of times. Choose dependant on searchForMost (Oxygen or CO2 Scrubber)
        if df_reports[currentBit].value_counts().max() == df_reports[currentBit].value_counts().min():
            search_criteria = '1' if searchForMost else '0'
        
        #pick only rows with search_criteria in selected column and put in a new DataFrame
        df_new = df_reports.loc[df_reports[currentBit] == search_criteria]
        return findRate(df_new, searchForMost, currentBit + 1)

def calculateLifeSupportRate(list_reports):
    #put list of list (str = list of characters) into dataframe
    df_reports = pd.DataFrame.from_records(list_reports)
    #drop last column containing '\n'
    df_reports.drop(df_reports.columns[len(df_reports.columns)-1], axis=1, inplace=True)

    listchr_oxygen_rate = findRate(df_reports, True, 0)
    listchr_co2scrubber_rate = findRate(df_reports, False, 0)

    #convert list of chars to string
    str_oxygen_rate = "".join(listchr_oxygen_rate)
    str_co2scrubber_rate = "".join(listchr_co2scrubber_rate)

    #convert binary string to numeric
    num_oxygen_rate = int(str_oxygen_rate, 2)
    num_co2scrubber_rate = int(str_co2scrubber_rate, 2)

    return num_oxygen_rate * num_co2scrubber_rate

infile = open(r'input.txt', "r")
listReports = infile.readlines()
infile.close()

print(str(calculateLifeSupportRate(listReports)))