import os, math, sys
import numpy as np

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day2')

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
        return [0] * 10
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

def Calculate_input(iArr_input, i_desired_output, i_inputMin, i_inputMax, i_Noun, i_Verb):
    print("Trying with noun " + str(i_Noun) + " and verb " + str(i_Verb))
    _iArrTemp = iArr_input.copy()
    _iArrTemp[1] = i_Noun
    _iArrTemp[2] = i_Verb
    _iIteratorOutput = intCode(_iArrTemp, 0)[0]

    if _iIteratorOutput != i_desired_output:
        #goal not reached
        print("Goal not reached, value pos 0 is equal to " + str(_iIteratorOutput))
        if i_Noun == i_inputMax:
            if i_Verb == i_inputMax:
                print("Limit reached, no values found for desired output of " + str(i_desired_output))
                return i_inputMax * 100 + i_inputMax
            else:
                #Reset noun, +1 verb
                i_Noun = i_inputMin
                i_Verb += 1
                return Calculate_input(iArr_input, i_desired_output, i_inputMin, i_inputMax, i_Noun, i_Verb)
        else:
            #+1 noun, try again
            i_Noun += 1
            return Calculate_input(iArr_input, i_desired_output, i_inputMin, i_inputMax, i_Noun, i_Verb)
    else:
        #goal reached
        return i_Noun * 100 + i_Verb

inp_array = np.loadtxt(fname='D2P1Input.txt', delimiter=',').astype(int)

noun_verb = Calculate_input(inp_array, 19690720, 0, 99, 0, 0)
print(noun_verb)

inp_array_tjell = np.loadtxt(fname='input.txt', delimiter=',').astype(int)
noun_verb = Calculate_input(inp_array_tjell, 19690720, 0, 99, 0, 97)
print(noun_verb)