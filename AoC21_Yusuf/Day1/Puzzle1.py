import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day1')

# Determine how many measurements are larger than previous
def countLargerThanPrevious(list_Depths):
	iCounter = iCurrentValue = 0	

	for _i in range(len(list_Depths)-1):
		iCurrentValue = list_Depths[_i]
		if iCurrentValue < list_Depths[_i + 1]:
			iCounter += 1		

	return iCounter

infile = open(r'input.txt', "r")
strListDepths = infile.readlines()
iListDepths = [int(i) for i in strListDepths]
infile.close()

print(str(countLargerThanPrevious(iListDepths)))