import os, math, sys
import numpy as np
from itertools import permutations

class IntCode:
	iArr_input = []
	i_position = 0
	i_input = 0
	i_output = 0
	i_relativebase = 0

	def __init__(self, i_inputFunc, iArr_inputarray):
		self.iArr_input = iArr_inputarray.copy()
		self.iArr_input = np.append(self.iArr_input, [0]*1000)
		self.i_position = 0
		self.i_input = i_inputFunc
		self.i_output = 0

	def Start_Intcode(self):
		_iOpcode = 0
		while(_iOpcode != 99):
			_iOpcode = self.iArr_input[self.i_position]
			_sParameterMode = ""
			if _iOpcode > 99:
				_sParameterMode = str(_iOpcode // 100)
				_iOpcode = _iOpcode % 100
				while len(_sParameterMode) < 3:
					_sParameterMode = f"0{_sParameterMode}"
			else:
				_sParameterMode = "000"
			print(_sParameterMode, _iOpcode, "with pos", self.i_position)
			if(_iOpcode == 99):
				print("intCode has reached 99.")
			elif(_iOpcode == 1):
				self.opcode_1(_sParameterMode)
			elif(_iOpcode == 2):
				self.opcode_2(_sParameterMode)
			elif(_iOpcode == 3):
				self.opcode_3(_sParameterMode)
			elif(_iOpcode == 4):
				self.opcode_4(_sParameterMode)
				print("Opcode 4 reached with output", str(self.i_output))
			elif(_iOpcode == 5):
				self.opcode_5(_sParameterMode)
			elif(_iOpcode == 6):
				self.opcode_6(_sParameterMode)
			elif(_iOpcode == 7):
				self.opcode_7(_sParameterMode)
			elif(_iOpcode == 8):
				self.opcode_8(_sParameterMode)
			elif(_iOpcode == 9):
				self.opcode_9(_sParameterMode)
			else:
				print("Something went wrong!")
				return -1
		return self.i_output

	def getParam(self, s_parameterMode, i_pos):
		if s_parameterMode[3-i_pos] == '2':
			return self.iArr_input[self.i_relativebase + self.iArr_input[self.i_position + i_pos]]
		else:
			return self.iArr_input[self.iArr_input[self.i_position + i_pos]] if s_parameterMode[3-i_pos] == '0' else self.iArr_input[self.i_position + i_pos]

	def setParam(self, s_parameterMode, i_pos, i_valueToStore):
		if s_parameterMode[3-i_pos] == '0':
			self.iArr_input[self.iArr_input[self.i_position + i_pos]] = i_valueToStore
		elif s_parameterMode[3-i_pos] == '1':
			self.iArr_input[self.i_position + i_pos] = i_valueToStore
		else: #2
			self.iArr_input[self.i_relativebase + self.iArr_input[self.i_position + i_pos]] = i_valueToStore

	def opcode_1(self, s_parameterMode):
		_iValue1 = self.getParam(s_parameterMode, 1)
		_iValue2 = self.getParam(s_parameterMode, 2)
		_iValue3 = _iValue1 + _iValue2
		self.setParam(s_parameterMode, 3, _iValue3)
		self.i_position += 4

	def opcode_2(self, s_parameterMode):
		_iValue1 = self.getParam(s_parameterMode, 1)
		_iValue2 = self.getParam(s_parameterMode, 2)
		_iValue3 = _iValue1 * _iValue2
		self.setParam(s_parameterMode, 3, _iValue3)
		self.i_position += 4

	def opcode_3(self, s_parameterMode):
		self.setParam(s_parameterMode, 1, self.i_input)
		self.i_position += 2

	def opcode_4(self, s_parameterMode):
		self.i_output = self.getParam(s_parameterMode, 1)
		self.i_position += 2

	def opcode_5(self, s_parameterMode):
		_iFirstParam = self.getParam(s_parameterMode, 1)
		_iSecondParam = self.getParam(s_parameterMode, 2)
		self.i_position = _iSecondParam if _iFirstParam != 0 else self.i_position + 3

	def opcode_6(self, s_parameterMode):
		_iFirstParam = self.getParam(s_parameterMode, 1)
		_iSecondParam = self.getParam(s_parameterMode, 2)
		self.i_position = _iSecondParam if _iFirstParam == 0 else self.i_position + 3

	def opcode_7(self, s_parameterMode):
		_iFirstParam = self.getParam(s_parameterMode, 1)
		_iSecondParam = self.getParam(s_parameterMode, 2)
		_iValueToStore = 1 if _iFirstParam < _iSecondParam else 0
		self.setParam(s_parameterMode, 3, _iValueToStore)
		self.i_position += 4

	def opcode_8(self, s_parameterMode):
		_iFirstParam = self.getParam(s_parameterMode, 1)
		_iSecondParam = self.getParam(s_parameterMode, 2)
		_iValueToStore = 1 if _iFirstParam == _iSecondParam else 0
		self.setParam(s_parameterMode, 3, _iValueToStore)
		self.i_position += 4

	def opcode_9(self, s_parameterMode):
		_iFirstParam = self.getParam(s_parameterMode, 1)
		self.i_relativebase += _iFirstParam
		print(self.i_relativebase)
		self.i_position += 2

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day9')

#Read input
inp_array = np.loadtxt(fname='D9Input.txt', delimiter=',', dtype='int64')
IC1 = IntCode(2, inp_array)
IC1.Start_Intcode()

print(sys.getrecursionlimit())