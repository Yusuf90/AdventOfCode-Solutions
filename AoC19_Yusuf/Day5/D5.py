import os, math, sys
import numpy as np

def intCode(iArr_input, i_position, i_input):
	#print(iArr_input[i_position])
	_iOpcode = iArr_input[i_position]
	_sParameterMode = ""
	if _iOpcode > 99:
		_sParameterMode = str(_iOpcode // 100)
		_iOpcode = _iOpcode % 100
		while len(_sParameterMode) < 3:
			_sParameterMode = f"0{_sParameterMode}"
	else:
		_sParameterMode = "000"
	if(_iOpcode == 99):
		return iArr_input
	elif(_iOpcode == 1):
		iArr_input = opcode_1(iArr_input, i_position, _sParameterMode)
		#print("Opcode 1 done, going to position " + str(i_position + 4))
		intCode(iArr_input, i_position + 4, i_input)
	elif(_iOpcode == 2):
		iArr_input = opcode_2(iArr_input, i_position, _sParameterMode)
		#print("Opcode 2 done, going to position " + str(i_position + 4))
		intCode(iArr_input, i_position + 4, i_input)
	elif(_iOpcode == 3):
		iArr_input = opcode_3(iArr_input, i_position, i_input)
		#print("Opcode 3 done, going to position " + str(i_position + 2))
		intCode(iArr_input, i_position + 2, i_input)
	elif(_iOpcode == 4):
		output_4 = opcode_4(iArr_input, i_position)
		print("Opcode 4 done, returns " + str(output_4))
		intCode(iArr_input, i_position + 2, i_input)
	elif(_iOpcode == 5):
		iHopTo = opcode_5(iArr_input, i_position, _sParameterMode)
		intCode(iArr_input, iHopTo, i_input)
	elif(_iOpcode == 6):
		iHopTo = opcode_6(iArr_input, i_position, _sParameterMode)
		intCode(iArr_input, iHopTo, i_input)
	elif(_iOpcode == 7):
		iArr_input = opcode_7(iArr_input, i_position, _sParameterMode)
		intCode(iArr_input, i_position + 4, i_input)
	elif(_iOpcode == 8):
		iArr_input = opcode_8(iArr_input, i_position, _sParameterMode)
		intCode(iArr_input, i_position + 4, i_input)
	else:
		print("Something went wrong!")
		return [0] * 10
	return iArr_input

def opcode_1(iArr_input, i_position, s_parameterMode):
	_iValue1 = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iValue2 = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	_iValue3 = _iValue1 + _iValue2
	if s_parameterMode[0] == '0':
		iArr_input[iArr_input[i_position + 3]] = _iValue3
	else:
		iArr_input[i_position + 3] = _iValue3
	return iArr_input

def opcode_2(iArr_input, i_position, s_parameterMode):
	_iValue1 = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iValue2 = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	_iValue3 = _iValue1 * _iValue2
	if s_parameterMode[0] == '0':
		iArr_input[iArr_input[i_position + 3]] = _iValue3
	else:
		iArr_input[i_position + 3] = _iValue3
	return iArr_input

def opcode_3(iArr_input, i_position, i_input):
	iArr_input[iArr_input[i_position + 1]] = i_input
	return iArr_input

def opcode_4(iArr_input, i_position):
	return iArr_input[iArr_input[i_position + 1]]

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day5')

#Read input
inp_array = np.loadtxt(fname='D5Input.txt', delimiter=',').astype(int)
print(inp_array)
intCode(inp_array, 0, 1)

def opcode_5(iArr_input, i_position, s_parameterMode):
	_iFirstParam = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iSecondParam = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	if _iFirstParam != 0:
		return _iSecondParam
	print("Opcode 5: Not jumping")
	return i_position + 3

def opcode_6(iArr_input, i_position, s_parameterMode):
	_iFirstParam = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iSecondParam = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	if _iFirstParam == 0:
		return _iSecondParam
	print("Opcode 6: Not jumping")
	return i_position + 3

def opcode_7(iArr_input, i_position, s_parameterMode):
	_iFirstParam = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iSecondParam = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	_iValueToStore = 1 if _iFirstParam < _iSecondParam else 0
	if s_parameterMode[0] == '0':
		iArr_input[iArr_input[i_position + 3]] = _iValueToStore
	else:
		iArr_input[i_position + 3] = _iValueToStore
	return iArr_input

def opcode_8(iArr_input, i_position, s_parameterMode):
	_iFirstParam = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	_iSecondParam = iArr_input[iArr_input[i_position + 2]] if s_parameterMode[1] == '0' else iArr_input[i_position + 2]
	_iValueToStore = 1 if _iFirstParam == _iSecondParam else 0
	if s_parameterMode[0] == '0':
		iArr_input[iArr_input[i_position + 3]] = _iValueToStore
	else:
		iArr_input[i_position + 3] = _iValueToStore
	return iArr_input

#Read input
inp_array = np.loadtxt(fname='D5Input.txt', delimiter=',').astype(int)
print(inp_array)
intCode(inp_array, 0, 5)