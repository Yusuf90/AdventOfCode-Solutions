import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day1')

def Calculate(s_input):
    i_temp = math.floor(s_input / 3) - 2
    if i_temp <= 0:
        return 0
    else:
        return i_temp + Calculate(i_temp)

def ReadAndCalc(s_inputFile):
    i_sum = 0
    infile = open(s_inputFile)
    for line in infile:
        i_sum = i_sum + Calculate(int(line))
    infile.close()
    return i_sum

print(str(ReadAndCalc(r'input.txt')))