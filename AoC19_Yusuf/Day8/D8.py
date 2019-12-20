import os, math, sys
import numpy as np

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day8')

#Read input
filetext = open("D8Input.txt", "r")
s_input = filetext.read()
filetext.close()

i_acreage = 25 * 6

sArr_pictures = [s_input[i:i+n] for i in range(0, len(s_input), n)]

i_FewestDigits = i_acreage
i_FewestPicture = sArr_pictures[0]
for sArr_picture in sArr_pictures:
	_iTempFewestDigits = sArr_picture.count('0')
	if _iTempFewestDigits < i_FewestDigits:
		i_FewestDigits = _iTempFewestDigits
		i_FewestPicture = sArr_picture