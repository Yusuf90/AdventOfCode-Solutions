import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day6')

#NOTE: Consider how many lantern each intial number might create taking amount of days into consideration, this would be wayyyy more efficient.
#NOTE: Function has been reconstructed following said suggestion (256 days would take too much memory in Python)
def amountLanternFish(list_initial_lantern, int_amount_days):    
    
    return 0

infile = open(r'test.txt', "r")
listInitialLantern = [int(x) for x in infile.read().split(',')]
infile.close()

print(str(amountLanternFish(listInitialLantern, 256)))