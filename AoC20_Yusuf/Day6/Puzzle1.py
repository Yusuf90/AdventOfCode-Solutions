import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day6')

def sumYesCounts(list_Groups):
	return 1

infile = open(r'input.txt', "r")
listOfGroups = infile.read().split("\n\n")
infile.close()

print(str(sumYesCounts(listOfGroups)))