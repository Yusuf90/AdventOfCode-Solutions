import sys
import os
import math
import pandas as pd

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day3')

def calculateHoriMulDepth(list_reports):
    #put list of list (str = list of characters) into dataframe
    df_reports = pd.DataFrame.from_records(list_reports)
    #drop last column containing '\n'
    df_reports.drop(df_reports.columns[len(df_reports.columns)-1], axis=1, inplace=True)

    #foreach column, idxmax each column; returning most frequent value and append to str_gamma_rate
    str_gamma_rate = ""
    for column in df_reports:        
        str_gamma_rate += df_reports[column].value_counts().idxmax()

    #Bit-wise invert the binary string for epsilon
    str_epsilon_rate = ''.join('1' if x == '0' else '0' for x in str_gamma_rate)

    #convert binary string to decimal representation
    num_gamma_rate = int(str_gamma_rate, 2)
    num_epsilon_rate = int(str_epsilon_rate, 2)

    return num_gamma_rate * num_epsilon_rate

infile = open(r'input.txt', "r")
listReports = infile.readlines()
infile.close()

print(str(calculateHoriMulDepth(listReports)))