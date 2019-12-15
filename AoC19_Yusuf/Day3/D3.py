import os, math, sys
import numpy as np

def processInstruction(iTup_Route, i_posX, i_posY, s_coordinate):
    iTupTemp = iTup_Route
    s_letter = s_coordinate[0]
    i_amount = int(s_coordinate[1:])
    for _iCounter in range(i_amount + 1):
        if s_letter == 'U':
            iTupTemp.append((i_posX, i_posY - _iCounter))            
        elif s_letter == 'R':
            iTupTemp.append((i_posX + _iCounter, i_posY))
        elif s_letter == 'D':
            iTupTemp.append((i_posX, i_posY + _iCounter))
        elif s_letter == 'L':
            iTupTemp.append((i_posX - _iCounter, i_posY))
        else:
            print("Unknown letter found, abort!")
    return iTupTemp[-1]

def calcCoordinates(inp):
    iTup_Route = []
    posX = 0
    posY = 0
    for i_instructionNumber in range(len(inp)):
        tupRes = processInstruction(iTup_Route, posX, posY, inp[i_instructionNumber])
        posX = tupRes[0]
        posY = tupRes[1]
    return iTup_Route

def closestManhattenDistance(inp1, inp2):
    iTup_Route1 = calcCoordinates(inp1)[1:]
    iTup_Route2 = calcCoordinates(inp2)[1:]
    iTup_CrossCoordinates = list(set(iTup_Route1) & set(iTup_Route2))
    first_tup = iTup_CrossCoordinates[0]
    iSmallestDistance = abs(first_tup[0]) + abs(first_tup[1])
    iTup_CrossCoordinates = iTup_CrossCoordinates[1:]
    for iTup in iTup_CrossCoordinates:
        iDistance =  abs(iTup[0]) + abs(iTup[1])
        if iSmallestDistance > iDistance:
            iSmallestDistance = iDistance
    return iSmallestDistance

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day3')

with open('D3P1Input.txt', 'r') as file_input:
    temp = file_input.read().splitlines()
    inp1 = temp[0].split(',')
    inp2 = temp[1].split(',')
    print(closestManhattenDistance(inp1, inp2))