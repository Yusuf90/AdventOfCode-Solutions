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

infile = open(r'input.txt', "r")
listOfRows = infile.readlines()
infile.close()

print(str(countTrees(listOfRows, len(listOfRows[0]) - 1, 3, 1, 0, 0)))