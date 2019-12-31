import os, math, sys
import numpy as np

#Get to current directory of puzzle
#os.chdir(os.getcwd() + r'\Day11')

#Read input
inp_array = np.loadtxt(fname='D11Input.txt', delimiter=',').astype(int)

print(inp_array)