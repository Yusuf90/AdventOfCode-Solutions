import os, math, sys
import numpy as np
from fractions import Fraction

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day10')

#Read input
filetext = open("D10Input.txt", "r")
s_input = filetext.read()
filetext.close()

print(s_input)

def translateInput(s_input):
	_iTupleMap = []
	_iWidthCounter = 0
	_iHeightCounter = 0
	_bAsteroid = False
	for c_data in s_input:
		if c_data == '\n':
			_iWidthCounter = 0
			_iHeightCounter += 1
			continue
		elif c_data == '#':
			yield (_iWidthCounter, _iHeightCounter)
		_iWidthCounter += 1

def reducefract(n, d):
	'''Reduces fractions. n is the numerator and d the denominator.'''
	numNegative = n < 0
	denNegative = d < 0
	def gcd(n, d):
		while d != 0:
			t = d
			d = n%d
			n = t
		return n
	greatest=gcd(n,d)
	n/=greatest
	d/=greatest
	if numNegative:
		return (-(abs(int(n))), -(abs(int(d)))) if denNegative else (-(abs(int(n))), abs(int(d)))
	else:
		return (abs(int(n)), -(abs(int(d)))) if denNegative else (abs(int(n)), abs(int(d)))

def asteroidSeen(iTupleMap_input, i_monitor_pos, i_asteroid_pos):
	_iTupleMap = iTupleMap_input.copy()
	_iWidthDiff = iTupleMap[i_monitor_pos][0] - iTupleMap[i_asteroid_pos][0]
	_iHeightDiff = iTupleMap[i_monitor_pos][1] - iTupleMap[i_asteroid_pos][1]
	
	_iVec = (0,0)
	if _iHeightDiff == 0:
		_iVec = (1,0) if _iWidthDiff > 0 else (-1,0)
	elif _iWidthDiff == 0:
		_iVec = (0,1) if _iHeightDiff > 0 else (0,-1)
	else:
		_iVec = reducefract(_iWidthDiff, _iHeightDiff)
	
	_iPointToTravel = (_iTupleMap[i_monitor_pos][0] , _iTupleMap[i_monitor_pos][1])
	_iPointTravelFrom = (_iTupleMap[i_asteroid_pos][0] , _iTupleMap[i_asteroid_pos][1])
	
	for _i in range(int(((_iWidthDiff / _iVec[0]) -1)) if _iVec[0] != 0 else int(((_iHeightDiff / _iVec[1]) -1))):
		if tuple(map(sum,zip(_iPointTravelFrom, (_iVec[0] * (_i + 1), _iVec[1] * (_i + 1))))) in _iTupleMap:
			return False
	return True

def totalAsteroidsSeen(iTupleMap_input, i_monitor_pos):
	_iTupleMap = iTupleMap_input.copy()
	_iAsteroidsSeen = 0
	for _iPoint in range(len(_iTupleMap)):
		if _iPoint == i_monitor_pos:
			continue
		_iAsteroidsSeen = _iAsteroidsSeen + 1 if asteroidSeen(_iTupleMap, i_monitor_pos, _iPoint) == True else _iAsteroidsSeen
	return _iAsteroidsSeen

def bestMonitorPosition(iTupleMap_input):
	_iTupleMap = iTupleMap_input.copy()
	_iMostSeen = 0
	_TupleBest = _iTupleMap[0]

	for _iIndex in range(len(_iTupleMap)):
		_iTempSeen = totalAsteroidsSeen(iTupleMap, _iIndex)
		if _iTempSeen > _iMostSeen:
			_iMostSeen = _iTempSeen
			_TupleBest = _iTupleMap[_iIndex]
	
	print("Best monitor position is", (_TupleBest[0], _TupleBest[1]), "with", _iMostSeen, "asteroids seen")
	return _TupleBest[0], _TupleBest[1]


iTupleMap = list(translateInput(s_input))

iBestPos = bestMonitorPosition(iTupleMap)
print(iBestPos)

#part 2

def calculateAngle(iTupStart, iTupEnd):
	_fAngle = math.atan2(iTupEnd[0] - iTupStart[0], iTupStart[1] - iTupEnd[1]) * 180 / math.pi
	if _fAngle < 0:
		return 360 + _fAngle
	return _fAngle

def defineTHVaporized(iTupleMap_input, iTuplePos, iAsteroidMaxCount):
	_iTupleMap = iTupleMap_input.copy()

	_iTupleMap.remove(iTuplePos)
	
	angles = sorted(
		((calculateAngle(iTuplePos, end), end) for end in _iTupleMap),
		key=lambda x: (x[0], abs(iTuplePos[0] - x[1][0]) + abs(iTuplePos[1] - x[1][1]))
	)

	print(angles)

	idx = 0
	last = angles.pop(idx)
	last_angle = last[0]
	cnt = 1

	while cnt < iAsteroidMaxCount and angles:
		if idx >= len(angles):
			idx = 0
			last_angle = None
		if last_angle == angles[idx][0]:
			idx += 1
			continue
		last = angles.pop(idx)
		last_angle = last[0]
		cnt += 1
	print('vaporized {}: {} {}'.format(cnt, last[1], last[1][0] * 100 + last[1][1]))
	return last[1][0] * 100 + last[1][1]

print(defineTHVaporized(iTupleMap, iBestPos, 200))
