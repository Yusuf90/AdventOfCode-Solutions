import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day6')

#NOTE: Consider how many lantern each intial number might create taking amount of days into consideration, this would be wayyyy more efficient.
def amountLanternFish(list_initial_lantern, int_amount_days):    
    #base case: Stop if no more days are left
    if(int_amount_days == 0):
        return len(list_initial_lantern)
    #general case: Subtract days, subtract 1 from each element and append new lanternfish if applicable
    else:
        #subtract 1 from each element and append new lanternfish if applicable
        _tempList = list_initial_lantern
        for _i, _fish in enumerate(_tempList):
            if _fish == 0:
                list_initial_lantern[_i] = 6
                list_initial_lantern.append(9)
            else:
                list_initial_lantern[_i] = list_initial_lantern[_i] - 1
        return amountLanternFish(list_initial_lantern, int_amount_days - 1)    

infile = open(r'input.txt', "r")
listInitialLantern = [int(x) for x in infile.read().split(',')]
infile.close()

print(str(amountLanternFish(listInitialLantern, 80)))