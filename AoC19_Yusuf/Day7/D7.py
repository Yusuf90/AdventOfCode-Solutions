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
	first_input_used = False
	return _iOutputAmp

def determineMaxSignal(iArr_input, i_Phase_Min, i_Phase_Max):
	_iLPhases = list(range(i_Phase_Min, i_Phase_Max))
	_iMaxSignal = 0
	_iMaxPhaseSetting = [0] * len(_iLPhases)
	for _iLCombo in permutations(_iLPhases):
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

print(determineMaxSignal(inp_array, 0, 5))

class Amplifier:
	iArr_AmpControlSoft = []
	i_position = 0
	i_input = 0
	b_phaseUsed = False
	b_haltReached = False
	i_phaseInput = 0
	i_output = 0
	s_name = ""

	def __init__(self, s_nameInput, i_phase, i_inputAmp, iArr_inputarray):
		self.iArr_AmpControlSoft = iArr_inputarray
		self.i_position = 0
		self.b_phaseUsed = False
		self.i_phaseInput = i_phase
		self.i_input = i_inputAmp
		self.i_output = 0
		self.s_name = s_nameInput

	def Start_Intcode(self):
		_iOpcode = self.iArr_AmpControlSoft[self.i_position]
		_sParameterMode = ""
		if _iOpcode > 99:
			_sParameterMode = str(_iOpcode // 100)
			_iOpcode = _iOpcode % 100
			while len(_sParameterMode) < 3:
				_sParameterMode = f"0{_sParameterMode}"
		else:
			_sParameterMode = "000"
		if(_iOpcode == 99):
			print("intCode has reached 99. End program!")
			self.b_haltReached = True
			return self.i_output
		elif(_iOpcode == 1):
			self.opcode_1(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 2):
			self.opcode_2(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 3):
			self.opcode_3(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 4):
			self.opcode_4(_sParameterMode)
			print("Opcode 4 reached for", self.s_name, "with output", str(self.i_output))
			return self.i_output
		elif(_iOpcode == 5):
			self.opcode_5(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 6):
			self.opcode_6(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 7):
			self.opcode_7(_sParameterMode)
			return self.Start_Intcode()
		elif(_iOpcode == 8):
			self.opcode_8(_sParameterMode)
			return self.Start_Intcode()
		else:
			print("Something went wrong!")
			return -1

	def opcode_1(self, s_parameterMode):
		_iValue1 = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iValue2 = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		_iValue3 = _iValue1 + _iValue2
		if s_parameterMode[0] == '0':
			self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 3]] = _iValue3
		else:
			self.iArr_AmpControlSoft[self.i_position + 3] = _iValue3
		self.i_position += 4

	def opcode_2(self, s_parameterMode):
		_iValue1 = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iValue2 = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		_iValue3 = _iValue1 * _iValue2
		if s_parameterMode[0] == '0':
			self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 3]] = _iValue3
		else:
			self.iArr_AmpControlSoft[self.i_position + 3] = _iValue3
		self.i_position += 4

	def opcode_3(self, s_parameterMode):
		_iValueToStore = self.i_input
		if self.b_phaseUsed == False:
			self.b_phaseUsed = True
			print("Opcode 3: Used phase setting once for", self.s_name)
			_iValueToStore = self.i_phaseInput
		if s_parameterMode[2] == '0':
			self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] = _iValueToStore
		else:
			self.iArr_AmpControlSoft[self.i_position + 1] = _iValueToStore
		self.i_position += 2

	def opcode_4(self, s_parameterMode):
		self.i_output = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		self.i_position += 2

	def opcode_5(self, s_parameterMode):
		_iFirstParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iSecondParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		if _iFirstParam != 0:
			self.i_position = _iSecondParam
		else:
			self.i_position += 3

	def opcode_6(self, s_parameterMode):
		_iFirstParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iSecondParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		if _iFirstParam == 0:
			self.i_position =  _iSecondParam
		else:
			self.i_position += 3

	def opcode_7(self, s_parameterMode):
		_iFirstParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iSecondParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		_iValueToStore = 1 if _iFirstParam < _iSecondParam else 0
		if s_parameterMode[0] == '0':
			self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 3]] = _iValueToStore
		else:
			self.iArr_AmpControlSoft[self.i_position + 3] = _iValueToStore
		self.i_position += 4

	def opcode_8(self, s_parameterMode):
		_iFirstParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 1]] if s_parameterMode[2] == '0' else self.iArr_AmpControlSoft[self.i_position + 1]
		_iSecondParam = self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 2]] if s_parameterMode[1] == '0' else self.iArr_AmpControlSoft[self.i_position + 2]
		_iValueToStore = 1 if _iFirstParam == _iSecondParam else 0
		if s_parameterMode[0] == '0':
			self.iArr_AmpControlSoft[self.iArr_AmpControlSoft[self.i_position + 3]] = _iValueToStore
		else:
			self.iArr_AmpControlSoft[self.i_position + 3] = _iValueToStore
		self.i_position += 4


def amplify_feedbackloop(iArr_input, iArr_phaseSetting):
	AmpA = Amplifier("AmpA", iArr_phaseSetting[0], 0, iArr_input)
	AmpB = Amplifier("AmpB", iArr_phaseSetting[1], AmpA.Start_Intcode(), iArr_input)
	AmpC = Amplifier("AmpC", iArr_phaseSetting[2], AmpB.Start_Intcode(), iArr_input)
	AmpD = Amplifier("AmpD", iArr_phaseSetting[3], AmpC.Start_Intcode(), iArr_input)
	AmpE = Amplifier("AmpE", iArr_phaseSetting[4], AmpD.Start_Intcode(), iArr_input)
	AmpA.i_input = AmpE.Start_Intcode()
	while AmpE.b_haltReached == False:
		AmpB.i_input = AmpA.Start_Intcode()
		AmpC.i_input = AmpB.Start_Intcode()
		AmpD.i_input = AmpC.Start_Intcode()
		AmpE.i_input = AmpD.Start_Intcode()
		AmpA.i_input = AmpE.Start_Intcode()
	print(AmpE.iArr_AmpControlSoft)
	return AmpE.i_output
#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day7')

#Read input
inp_array = np.loadtxt(fname='D7TestInput.txt', delimiter=',').astype(int)

#print(determineMaxSignal(inp_array, 0, 5))

#inp_array = np.loadtxt(fname='D7TestInput.txt', delimiter=',').astype(int)

print(amplify_feedbackloop(inp_array, [9,8,7,6,5]))

#print(determineMaxSignal_feedbackloop(inp_array, 5, 5))