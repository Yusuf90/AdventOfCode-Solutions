import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day5')

def totalSeats(s_SampleSeat, i_half):
	return 2**len(s_SampleSeat[:i_half]) * 2**len(s_SampleSeat[i_half:])

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

def calculateHighestAndLowestSeatID(list_BPasses):
	_iLowestSeatID = totalSeats(list_BPasses[0], 7)
	_iHighestSeatID = 0
	for _sBPass in list_BPasses:
		_iTempSeatID = calculateSeatID(_sBPass)
		_iHighestSeatID = _iTempSeatID if _iTempSeatID > _iHighestSeatID else _iHighestSeatID
		_iLowestSeatID = _iTempSeatID if _iTempSeatID < _iLowestSeatID else _iLowestSeatID
	return _iLowestSeatID, _iHighestSeatID

def returnEmptySeats(list_BPasses):
	_listAvailableSeats = list(range(totalSeats(list_BPasses[0], 7)))
	for _sBPass in list_BPasses:
		_listAvailableSeats.remove(calculateSeatID(_sBPass))
	_iLowest, _iHighest = calculateHighestAndLowestSeatID(list_BPasses)
	_listAvailableSeats = [availableSeat for availableSeat in _listAvailableSeats if _iLowest < availableSeat < _iHighest]
	return _listAvailableSeats

infile = open(r'input.txt', "r")
listOfBoardingPasses = infile.read().splitlines()
infile.close()

print(returnEmptySeats(listOfBoardingPasses))