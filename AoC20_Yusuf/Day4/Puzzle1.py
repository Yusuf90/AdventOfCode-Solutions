import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day4')

def countValidPassports(list_passports, list_required, list_optional):
	_iTotalValid = 0
	for _sPassport in list_passports:
		_iTotalValid += 1 if validatePassport(_sPassport.split(), list_required, list_optional) else 0
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

infile = open(r'input.txt', "r")
listOfPassports = infile.read().split("\n\n")
infile.close()

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = ["cid"]

print(str(countValidPassports(listOfPassports, required, optional)))