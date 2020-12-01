import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day1')

def CalcNumber(set_Ints, i_NumberToFind, totalNumbers):
    _iReturn = 0
    for _int in set_Ints:
        if totalNumbers == 2:
            if i_NumberToFind - _int in set_Ints:
                return _int * (i_NumberToFind - _int)
        else:
            _iReturn =  CalcNumber(set_Ints, i_NumberToFind - _int, totalNumbers - 1)
            if _iReturn != 0:
                return _iReturn * _int
    return 0

infile = open(r'input.txt', "r")
listOfInts = infile.readlines()
setOfInts = set([int(i) for i in listOfInts])
infile.close()

print(str(CalcNumber(setOfInts, 2020, 3)))