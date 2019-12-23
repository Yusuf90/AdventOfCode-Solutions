import os, math, sys
import numpy as np

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day8')

#Read input
filetext = open("D8Input.txt", "r")
s_input = filetext.read()
filetext.close()

i_acreage = 25 * 6

sArr_pictures = [s_input[i:i+i_acreage] for i in range(0, len(s_input), i_acreage)]

i_FewestDigits = i_acreage
i_FewestPicture = sArr_pictures[0]
for sArr_picture in sArr_pictures:
	_iTempFewestDigits = sArr_picture.count('0')
	if _iTempFewestDigits < i_FewestDigits:
		i_FewestDigits = _iTempFewestDigits
		i_FewestPicture = sArr_picture

i_num1_digits = i_FewestPicture.count('1')
i_num2_digits = i_FewestPicture.count('2')

print(i_num1_digits * i_num2_digits)

def decode_picture(s_input, iTotalWidth, iTotalHeight):
	sArr_pictures = [s_input[i:i+(iTotalWidth * iTotalHeight)] for i in range(0, len(s_input), iTotalWidth * iTotalHeight)]
	_iArrTemp = ""
	for iPixel in range(iTotalWidth * iTotalHeight):
			for sArr_picture in sArr_pictures:
				if sArr_picture[iPixel] != '2':
					_iArrTemp += sArr_picture[iPixel]
					break
	_iArrSplit = []
	for index in range(0, len(_iArrTemp), iTotalWidth):
		_iArrSplit.append(_iArrTemp[index : index + iTotalWidth])
	return _iArrSplit

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day8')

#Read input
filetext = open("D8Input.txt", "r")
s_input = filetext.read()
filetext.close()

print("\n".join(decode_picture(s_input, 25, 6)))