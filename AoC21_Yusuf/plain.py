import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day1')

def countLargerThanPrevious(list_Groups):
	return 1

infile = open(r'input.txt', "r")
listOfGroups = infile.readlines()
infile.close()

print(str(countLargerThanPrevious(listOfGroups)))