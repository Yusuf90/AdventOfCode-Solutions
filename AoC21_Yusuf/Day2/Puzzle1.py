import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day2')

def calculateHoriMulDepth(list_instructions):
    _iHorizontal = _iDepth = 0
    for instruction in list_instructions:
        tup_temp = instruction.split(' ')
        if(tup_temp[0] == 'forward'):
            _iHorizontal += int(tup_temp[1])
        elif(tup_temp[0] == 'down'):
            _iDepth += int(tup_temp[1])
        elif(tup_temp[0] == 'up'):
            _iDepth -= int(tup_temp[1])
    return _iHorizontal * _iDepth

infile = open(r'input.txt', "r")
listInstructions = infile.readlines()
infile.close()

print(str(calculateHoriMulDepth(listInstructions)))