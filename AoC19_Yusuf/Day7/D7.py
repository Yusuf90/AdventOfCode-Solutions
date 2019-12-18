import os, math, sys
import numpy as np
from itertools import permutations

first_input_used = False

def intCode(iArr_input, i_position, i_inputPhase, i_inputOutputAmp):
	global first_input_used
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
		print("intCode has reached 99 without Opcode 4 execution, something went wrong!")
		return -1
	elif(_iOpcode == 1):
		iArr_input = opcode_1(iArr_input, i_position, _sParameterMode)
		#print("Opcode 1 done, going to position " + str(i_position + 4))
		return intCode(iArr_input, i_position + 4, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 2):
		iArr_input = opcode_2(iArr_input, i_position, _sParameterMode)
		#print("Opcode 2 done, going to position " + str(i_position + 4))
		return intCode(iArr_input, i_position + 4, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 3):
		if first_input_used == False:
			iArr_input = opcode_3(iArr_input, i_position, i_inputPhase, _sParameterMode)
			first_input_used = True
		else:
			iArr_input = opcode_3(iArr_input, i_position, i_inputOutputAmp, _sParameterMode)
		#print("Opcode 3 done, going to position " + str(i_position + 2))
		return intCode(iArr_input, i_position + 2, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 4):
		output_4 = opcode_4(iArr_input, i_position, _sParameterMode)
		print("Opcode 4 done, returns " + str(output_4))
		if output_4 != 0:
			if(iArr_input[i_position + 2] % 100 == 99):
				print("Opcode 4 followed by halt means output")
				return output_4
			print("Opcode 4 did not return 0, something went wrong!")
			return -1
		return intCode(iArr_input, i_position + 2, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 5):
		iHopTo = opcode_5(iArr_input, i_position, _sParameterMode)
		return intCode(iArr_input, iHopTo, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 6):
		iHopTo = opcode_6(iArr_input, i_position, _sParameterMode)
		return intCode(iArr_input, iHopTo, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 7):
		iArr_input = opcode_7(iArr_input, i_position, _sParameterMode)
		return intCode(iArr_input, i_position + 4, i_inputPhase, i_inputOutputAmp)
	elif(_iOpcode == 8):
		iArr_input = opcode_8(iArr_input, i_position, _sParameterMode)
		return intCode(iArr_input, i_position + 4, i_inputPhase, i_inputOutputAmp)
	else:
		print("Something went wrong!")
		return -1

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

def opcode_3(iArr_input, i_position, i_input, s_parameterMode):
	if s_parameterMode[2] == '0':
		iArr_input[iArr_input[i_position + 1]] = i_input
	else:
		iArr_input[i_position + 1] = i_input
	return iArr_input

def opcode_4(iArr_input, i_position, s_parameterMode):
	_iFirstParam = iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]
	return iArr_input[iArr_input[i_position + 1]] if s_parameterMode[2] == '0' else iArr_input[i_position + 1]

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

def amplify(iArr_input, iArr_phaseSetting):
	global first_input_used
	_iOutputAmp = 0
	for _iPhase in iArr_phaseSetting:
		_iArrTemp = iArr_input.copy()
		first_input_used = False
		_iOutputAmp = intCode(_iArrTemp, 0, _iPhase, _iOutputAmp)
		if _iOutputAmp == -1:
			print("Something went wrong!")
	return _iOutputAmp

def determineMaxSignal(iArr_input, i_Phase_length):
	_iMaxSignal = 0
	_iMaxPhaseSetting = [0] * i_Phase_length
	for _iLCombo in permutations(list(range(i_Phase_length))):
		_iTempSignal = amplify(iArr_input, _iLCombo)
		if _iTempSignal > _iMaxSignal:
			_iMaxSignal = _iTempSignal
			_iMaxPhaseSetting = _iLCombo
	print("With phase setting " + str(_iMaxPhaseSetting))
	print("Max signal output is " + str(_iMaxSignal))
	return _iMaxSignal

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day7')

#Read input
inp_array = np.loadtxt(fname='D7Input.txt', delimiter=',').astype(int)

print(determineMaxSignal(inp_array, 5))