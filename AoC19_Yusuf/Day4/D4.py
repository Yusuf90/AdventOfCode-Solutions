import os, math, sys
import numpy as np

def criteria_sixdigit(i_input):
	_iCount = 0
	while i_input > 0:
		i_input = i_input // 10
		_iCount += 1
	if _iCount == 6:
		return True
	else:
		return False

def criteria_adjacent(i_input):
	_sLDigits = list(str(i_input))
	for _index in range(len(_sLDigits[:-1])):
		if _sLDigits[_index] == _sLDigits[_index + 1]:
			return True
	return False

def criteria_nvrDecrease(i_input):
	_sLDigits = list(str(i_input))
	for _index in range(len(_sLDigits[:-1])):
		if _sLDigits[_index] > _sLDigits[_index + 1]:
			return False
	return True

def validate_input(i_input):
	return criteria_adjacent(i_input) and criteria_sixdigit(i_input) and criteria_nvrDecrease(i_input)

def count_valid(i_inputStart, i_inputEnd):
	_iCounter = 0
	for _iIteration in range(i_inputStart, i_inputEnd):
		if validate_input(_iIteration) == True:
			_iCounter += 1
	return _iCounter

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day4')

inp_array = np.loadtxt(fname='D4Input1.txt', delimiter='-').astype(int)

print(count_valid(inp_array[0], inp_array[1]))

def criteria_adjacent2(i_input):
	_sLDigits = list(str(i_input))
	for _index in range(len(_sLDigits[:-1])):
		if _sLDigits[_index] == _sLDigits[_index + 1]:
			#leftside
			if _index == 0:
				if _sLDigits[_index + 1] != _sLDigits[_index + 2]:
					return True
			#rightside
			elif (_index + 2) == len(_sLDigits):
				if _sLDigits[_index - 1] != _sLDigits[_index]:
					return True
			#mid
			elif _sLDigits[_index - 1] != _sLDigits[_index] and _sLDigits[_index + 1] != _sLDigits[_index + 2]:
				return True
	return False

def validate_input2(i_input):
	return criteria_adjacent2(i_input) and criteria_sixdigit(i_input) and criteria_nvrDecrease(i_input)

def count_valid2(i_inputStart, i_inputEnd):
	_iCounter = 0
	for _iIteration in range(i_inputStart, i_inputEnd):
		if validate_input2(_iIteration) == True:
			_iCounter += 1
	return _iCounter

print(count_valid2(inp_array[0], inp_array[1]))
