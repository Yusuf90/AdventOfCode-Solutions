import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day2')

def countValidity(list_strings):
	_iTotal = 0
	for str_item in list_strings:
		_iTotal += 1 if checkValidity(str_item) else 0
	return _iTotal

def checkValidity(string_item):
	_strItems = string_item.split(" ")
	_iMin, _iMax = map(int, _strItems[0].split("-"))
	return True if _iMin <= _strItems[2].count(_strItems[1][0]) <= _iMax else False

infile = open(r'input.txt', "r")
listOfStrings = infile.readlines()
infile.close()

print(str(countValidity(listOfStrings)))
