import sys
import os
import math
import string

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day4')

def countValidPassports(list_passports, list_required, list_optional):
	_iTotalValid = 0
	for _sPassport in list_passports:
		#split() with no argument splits on ANY whitespace.
		if validatePassport(_sPassport.split(), list_required, list_optional):
			_iTotalValid += 1 if validateValues(_sPassport.split()) else 0
	return _iTotalValid

def validatePassport(list_passportdetails, list_required, list_optional):
	#only need 1st part of details
	list_passportdetails = [_passport.split(":")[0] for _passport in list_passportdetails]
	#case 1: total items < required, return False
	if len(list_passportdetails) < len(list_required): return False
	#case 2: total items == required
	if len(list_passportdetails) == len(list_required):
		#case 2a: Has an optional one (which means its missing a required one)
		return not any(optional in list_passportdetails for optional in list_optional)

	#case 3: total items > required (check not needed if assumption in 2b is true)
	return all(required in list_passportdetails for required in list_required)

def validateValues(list_passportdetails):
	dictOfPassport = { _passport.split(":")[0] : _passport.split(":")[1] for _passport in list_passportdetails }
	#byr 
	if not 1920 <= int(dictOfPassport.get("byr")) <= 2002: return False
	#iyr 
	if not 2010 <= int(dictOfPassport.get("iyr")) <= 2020: return False
	#eyr 
	if not 2020 <= int(dictOfPassport.get("eyr")) <= 2030: return False
	#hgt 
	_sHeight = dictOfPassport.get("hgt")
	if _sHeight[-2:] == "cm":
		if not 150 <= int(_sHeight[:-2]) <= 193: return False
	elif _sHeight[-2:] == "in":
		if not 59 <= int(_sHeight[:-2]) <= 76: return False
	else:
		return False
	#hcl 
	_sHairColor = dictOfPassport.get("hcl")
	if len(_sHairColor) != 7 or _sHairColor[0] != "#": return False
	if not all(_char in string.hexdigits for _char in _sHairColor[1:]): return False
	#ecl 
	_listValidEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if not dictOfPassport.get("ecl") in _listValidEyeColors: return False
	#pid 
	if not all(_char in string.digits for _char in dictOfPassport.get("pid")) or len(dictOfPassport.get("pid")) != 9: return False
	#all pass
	return True

infile = open(r'input.txt', "r")
listOfPassports = infile.read().split("\n\n")
infile.close()

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = ["cid"]

print(str(countValidPassports(listOfPassports, required, optional)))