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
	_iFirst, _iSecond = map(int, _strItems[0].split("-"))
	return (_strItems[2][_iFirst - 1] == _strItems[1][0]) ^ (_strItems[2][_iSecond - 1] == _strItems[1][0])

infile = open(r'input.txt', "r")
listOfStrings = infile.readlines()
infile.close()

print(str(countValidity(listOfStrings)))
