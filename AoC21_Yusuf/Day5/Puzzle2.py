import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day5')

def countOverlap(list_instructions, int_amount_lines, int_dimensions):
    #create matrix with zero's
    ocean_floor = [ [ 0 for i in range(int_dimensions) ] for j in range(int_dimensions) ]
    _counter = 0
    for _instruction in list_instructions:
        _arrInstruction = _instruction.split(" -> ")
        _arrFirst = [int(x) for x in _arrInstruction[0].split(",")]        
        _arrSecond = [int(x) for x in _arrInstruction[1].split(",")]
        _arrPoints = []
        #Diagonal line
        if _arrFirst[0] != _arrSecond[0] and _arrFirst[1] != _arrSecond[1]:
            _iStepOnX = -1 if _arrFirst[0] > _arrSecond[0] else 1
            _iStepOnY = -1 if _arrFirst[1] > _arrSecond[1] else 1
            for _i in range(abs(_arrFirst[0] - _arrSecond[0]) + 1):
                _coordinateToAdd = [_arrFirst[0] + (_i * _iStepOnX), _arrFirst[1] + ( _i * _iStepOnY)]
                _arrPoints.append(_coordinateToAdd)
        #Vertical line
        elif _arrFirst[0] == _arrSecond[0]:
            for _i in range(abs(_arrFirst[1] - _arrSecond[1]) + 1):
                _coordinateToAdd = [_arrFirst[0], _arrFirst[1] + _i] if _arrFirst[1] <= _arrSecond[1] else [_arrFirst[0], _arrFirst[1] - _i]
                _arrPoints.append(_coordinateToAdd)
        #Horizontal line
        elif _arrFirst[1] == _arrSecond[1]:
            for _i in range(abs(_arrFirst[0] - _arrSecond[0]) + 1):
                _coordinateToAdd = [_arrFirst[0] + _i, _arrFirst[1]] if _arrFirst[0] <= _arrSecond[0] else [_arrFirst[0] - _i, _arrFirst[1]]
                _arrPoints.append(_coordinateToAdd)  
        for _point in _arrPoints:
            ocean_floor[_point[1]][_point[0]] += 1
            if ocean_floor[_point[1]][_point[0]] == int_amount_lines:
                _counter += 1
    return _counter

infile = open(r'input.txt', "r")
listInstructions = infile.read().splitlines()
infile.close()

#print(str(countOverlap(listInstructions, 2, 10)))
print(str(countOverlap(listInstructions, 2, 999)))