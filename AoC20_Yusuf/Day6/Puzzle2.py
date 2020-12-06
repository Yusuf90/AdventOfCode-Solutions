import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day6')

infile = open(r'input.txt', "r")
listOfPassports = infile.read().split("\n\n")
infile.close()