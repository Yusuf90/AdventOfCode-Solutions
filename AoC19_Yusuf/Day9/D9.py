import os, math, sys
import numpy as np
from itertools import permutations

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
			print("intCode has reached 99. End program for", self.s_name)
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