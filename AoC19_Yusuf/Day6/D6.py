import os, math, sys
import numpy as np
import pandas as pd

COL_OBJECT = 'Object'
COL_ORBIT_BY = 'OrbitBy'
COL_TOTAL_ORBITS = 'TotalOrbits'

def readDataFrame(s_filename):
    #Get to current directory of puzzle
    #os.chdir(os.getcwd() + r'\Day6')
    _sLInput = [] 
    _sLInputCol1 = []
    _sLInputCol2 = []
    with open(s_filename, 'r') as file_input:
        _sLInput = file_input.read().splitlines()
    for _sInput in _sLInput:
        _sLInputCol1.append(_sInput.split(')')[0])
        _sLInputCol2.append(_sInput.split(')')[1])
    return pd.DataFrame(
        {COL_OBJECT: _sLInputCol2,
        COL_ORBIT_BY: _sLInputCol1
        })

df_objects = readDataFrame('D6Input.txt')

def calcOrbits(df_input):
    _iLenDf = len(df_input[COL_OBJECT])
    df_input[COL_TOTAL_ORBITS] = [0] * _iLenDf
    for _iCurrentIndex in range(len(df_input[COL_OBJECT])):
        _sObject = df_input.iloc[_iCurrentIndex][COL_OBJECT]
        _iCounter = 1
        _sOrbitBy = df_input.iloc[_iCurrentIndex][COL_ORBIT_BY]
        while _sOrbitBy in list(df_input[COL_OBJECT]):
            _iCounter += 1
            _iNewIndex = df_input.loc[df_input[COL_OBJECT] == _sOrbitBy].index[0]
            _sOrbitBy = df_input.iloc[_iNewIndex][COL_ORBIT_BY]
        df_input.at[_iCurrentIndex, COL_TOTAL_ORBITS] = _iCounter
        print(str(_iCurrentIndex) + "//" + str(_iLenDf - 1))
    return df_input

#df_objects = calcOrbits(df_objects)
#print(df_objects[COL_TOTAL_ORBITS].sum())

def calcOrbitPath(df_input, s_object):
    _sLOutput = []
    _iStartIndex = df_input.loc[df_input[COL_OBJECT] == s_object].index[0]
    while s_object in list(df_input[COL_OBJECT]):
        _iNewIndex = df_input.loc[df_input[COL_OBJECT] == s_object].index[0]
        s_object = df_input.iloc[_iNewIndex][COL_ORBIT_BY]
        _sLOutput.append(s_object)
    return _sLOutput

def calcOrbitalTransfers(df_input, s_object_1, s_object_2):
    _sLObj1 = calcOrbitPath(df_objects, s_object_1)
    _sLObj2 = calcOrbitPath(df_objects, s_object_2)
    _ssLObj2 = set(_sLObj2)
    _iIndexObj1 = [i for i, item in enumerate(_sLObj1) if item in _ssLObj2][0]
    _sCross = _sLObj1[_iIndexObj1]
    return _sLObj2.index(_sCross) + _sLObj1.index(_sCross)

print(calcOrbitalTransfers(df_objects, 'YOU', 'SAN'))


