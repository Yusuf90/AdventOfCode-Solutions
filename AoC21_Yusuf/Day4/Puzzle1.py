import sys
import os
import math

#Get to current directory of puzzle
os.chdir(os.getcwd() + r'\Day4')

#Creates list of bingo sheets that contains tuples(number, boolean): [[22, False], [13, False], ...]
def createBingoSheets(list_split_lined, int_size):
    _listBingoSheets = []
    _listBingoSheet = []
    for _element in list_split_lined:
        if _element == "":
            _listBingoSheet = []
            continue        
        _tempNumArray = [(int(x), False) for x in _element.split()]
        _listBingoSheet.append(_tempNumArray)
        if len(_listBingoSheet) == int_size:
            _listBingoSheets.append(_listBingoSheet)
    return _listBingoSheets

#Check if 2nd element of Tuple has a row of True's (Vertical and Horizontal)
def checkBingoSheet(list_bingo_sheet):
    #check horizontal
    for _row in list_bingo_sheet:
        if sum([item[1] for item in _row if item[1] == True]) == 5:
            return True
    #check vertical (by transposing the sheet first)
    transposed_sheet = list(zip(*list_bingo_sheet))
    for _row in transposed_sheet:
        if sum([item[1] for item in _row if item[1] == True]) == 5:
            return True
    return False

#Check if bingo sheet contains bingo pull, if so, put 2nd element of found tuple to True
def crossNumber(list_bingo_sheet, int_bingopull):
    #Find item and set item[1] = True if found
    _elementFound = False
    for _x, _row in enumerate(list_bingo_sheet):
        if _elementFound:
            break
        for _y, _element in enumerate(_row):
            if _element[0] == int_bingopull:
                list_bingo_sheet[_x][_y] = (int_bingopull, True)
                _elementFound = True
                break
    return list_bingo_sheet

#Sum all numbers that are (x, False) where x is the numbers to be summed up
def sumUnmarked(list_bingo_sheet):
    _sum = 0
    for _row in list_bingo_sheet:
        _sum += sum([item[0] for item in _row if item[1] == False])
    return _sum

def calculateWinningBoardSum(list_bingo_sheets, list_bingo_pulls):
    for _bingopull in list_bingo_pulls:
        for _i, _bingoSheet in enumerate(list_bingo_sheets):            
            list_bingo_sheets[_i] = crossNumber(_bingoSheet, _bingopull)
            if checkBingoSheet(list_bingo_sheets[_i]):
                return sumUnmarked(list_bingo_sheets[_i]) * _bingopull
    return 0 #no winner found??

infile = open(r'input.txt', "r")
listBingoPulls = [int(x) for x in infile.readline().strip().split(',')]
listSplitLined = infile.read().splitlines()
infile.close()

listBingoSheets = createBingoSheets(listSplitLined, 5)
print(str(calculateWinningBoardSum(listBingoSheets, listBingoPulls)))