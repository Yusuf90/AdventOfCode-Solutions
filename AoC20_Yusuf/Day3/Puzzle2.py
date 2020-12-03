import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day3')

def countTrees(grid, gridWidth, stepX, stepY, posX, posY):
	#No need to exclude first position, since assignment guarantees you start on '.'
	_iAddTreeCount = 1 if grid[posY][posX] == "#" else 0
	#base case
	if(posY == len(grid) - 1):
		return _iAddTreeCount
	#general case
	else:
		posY += stepY
		posX = posX + stepX - gridWidth if posX + stepX >= gridWidth else posX + stepX
		return _iAddTreeCount + countTrees(grid, gridWidth, stepX, stepY, posX, posY)

def multiplySlopeResults(listOfSlopes, grid, startPos):
	_iResult = 1 #for multiply purposes
	for _tuple in listOfSlopes:
		_iResult *= countTrees(grid, len(grid[0]) - 1, _tuple[0], _tuple[1], startPos[0], startPos[1])
	return _iResult

infile = open(r'input.txt', "r")
listOfRows = infile.readlines()
infile.close()

listOfSlopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(str(multiplySlopeResults(listOfSlopes, listOfRows, (0,0))))