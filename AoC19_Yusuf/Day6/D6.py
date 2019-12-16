import os, math, sys
import numpy as np
import pandas as pd

def readDataFrame(s_filename):
    #Get to current directory of puzzle
    os.chdir(os.getcwd() + r'\Day6')

    #Read input
    sL_input = [] 
    sL_inputCol1 = []
    sL_inputCol2 = []
    with open(s_filename, 'r') as file_input:
        sL_input = file_input.read().splitlines()

    for _sInput in sL_input:
        sL_inputCol1.append(_sInput.split(')')[0])
        sL_inputCol2.append(_sInput.split(')')[1])
    return pd.DataFrame(
        {'Object': sL_inputCol2,
        'OrbitBy': sL_inputCol1
        })

print(readDataFrame('D6Input.txt'))
