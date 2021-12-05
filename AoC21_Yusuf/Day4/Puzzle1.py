import sys
import os
import math
import pandas as pd

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day4')

def createBingoSheets(list_split_lined, int_size):
    _listBingoSheets = []
    for _i in range(len(list_split_lined), int_size):
        


    return _listBingoSheets

def calculateHoriMulDepth(listBingoPulls):
    

    return 1

infile = open(r'test.txt', "r")
listBingoPulls = infile.readline().strip().split(',')
listSplitLined = infile.read().splitlines()
infile.close()

listBingoSheets = createBingoSheets(listSplitLined, 5)
print(str(calculateHoriMulDepth(listBingoPulls)))