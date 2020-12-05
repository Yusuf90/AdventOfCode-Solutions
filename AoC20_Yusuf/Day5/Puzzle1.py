import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day5')

def decodeToNumber(str_input, c_FirstIndicator, c_SecondIndicator):
	_iRangeStart = 0
	_iRangeEnd = 2**len(str_input)
	for _cIndicator in str_input:
		_iValueToCut = (_iRangeEnd - _iRangeStart) / 2
		if _cIndicator == c_FirstIndicator:
			_iRangeEnd -= _iValueToCut
		else: #_cIndicator == c_SecondIndicator
			_iRangeStart += _iValueToCut
	return int(_iRangeStart) #or _iRangeEnd

def calculateSeatID(s_BPass):
	_iRow = decodeToNumber(s_BPass[:7], 'F', 'B')
	_iColumn = decodeToNumber(s_BPass[7:], 'L', 'R')
	return (_iRow * 2**len(s_BPass[7:])) + _iColumn

def calculateHighestSeatID(list_BPasses):
	_iHighestSeatID = 0
	for _sBPass in list_BPasses:
		_iTempSeatID = calculateSeatID(_sBPass)
		_iHighestSeatID = _iTempSeatID if _iTempSeatID > _iHighestSeatID else _iHighestSeatID
	return _iHighestSeatID

infile = open(r'input.txt', "r")
listOfBoardingPasses = infile.read().splitlines()
infile.close()

print(calculateHighestSeatID(listOfBoardingPasses))