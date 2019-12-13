import os, math, sys
import numpy as np

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day2')

#Read input
inp_array = np.loadtxt(fname='D2P1Input.txt', delimiter=',').astype(int)
print(inp_array)

#Change values in array, [1] to 12, [2] to 2
inp_array[1] = 12
inp_array[2] = 2
print(inp_array)

def intCode(iArr_input, i_position):
    if(iArr_input[i_position] == 99):        
        return iArr_input
    elif(iArr_input[i_position] == 1):
        iArr_input = opcode_1(iArr_input, i_position)
        #print("Opcode 1 done, going to position " + str(i_position + 4) + " with array " + str(iArr_input))
        intCode(iArr_input, i_position + 4)
    elif(iArr_input[i_position] == 2):
        iArr_input = opcode_2(iArr_input, i_position)
        #print("Opcode 2 done, going to position " + str(i_position + 4) + " with array " + str(iArr_input))
        intCode(iArr_input, i_position + 4)
    else:
        print("Something went wrong!")
        return 0
    return iArr_input

def opcode_1(iArr_input, i_position):
    _iValue1 = iArr_input[iArr_input[i_position + 1]]
    _iValue2 = iArr_input[iArr_input[i_position + 2]]
    _iValue3 = _iValue1 + _iValue2
    iArr_input[iArr_input[i_position + 3]] = _iValue3
    return iArr_input

def opcode_2(iArr_input, i_position):
    _iValue1 = iArr_input[iArr_input[i_position + 1]]
    _iValue2 = iArr_input[iArr_input[i_position + 2]]
    _iValue3 = _iValue1 * _iValue2
    iArr_input[iArr_input[i_position + 3]] = _iValue3
    return iArr_input

pos1 = intCode(inp_array, 0)[0]
print(pos1)