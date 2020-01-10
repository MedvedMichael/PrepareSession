import random


def generateMatrix():  # create matrix nxn
    n = int(input("Input n: "))
    matrix = [[int(random.uniform(-100, 100)) for j in range(0, n)] for i in range(0, n)]
    print("Start matrix: ")
    printTwoDimentionalArray(matrix)
    return matrix


def mirrorMatrix(matrix):  # mirror matrix by diagonal
    for i in range(1, len(matrix)):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print("Mirrored matrix: ")
    printTwoDimentionalArray(matrix)


def printTwoDimentionalArray(matrix):
    for row in matrix:
        print(row)
    print()


def deleteColumn(matrix):  # delete column with index "columnIndex", input from keyboard
    columnIndex = int(input("Input number of column: "))
    for row in matrix:
        del row[columnIndex]
    print("Current matrix: ")
    printTwoDimentionalArray(matrix)


def generateLines(matrix):  # generate lines from deltaArrays
    arrayOfLines = []

    for row in matrix:
        deltaArr = []
        for i in range(0, len(row) - 1):  # create array from minus of neighbours in the row
            deltaArr.append(row[i + 1] - row[i])
        deltaArr = sortArray(deltaArr)
        line = getLineFromArray(deltaArr)
        arrayOfLines.append(line)
    return arrayOfLines


def getLineFromArray(array):  # generate line (string) from an array by spaces
    line = ""
    for element in array:
        line += str(element) + " "
    return line


def sortArray(array):  # sorts array to put negative values to the start
    deltaList = []
    i = 0
    while i < len(array):
        if array[i] < 0:
            deltaList.append(array[i])
            del array[i]
            i -= 1
        i += 1

    deltaList.extend(array)
    return deltaList


def sortArrayOfLines(lines):  # sort an array of line according to their lengths
    for i in range(0, len(lines) - 1):
        for j in range(i + 1, len(lines)):
            if len(lines[i]) > len(lines[j]):
                lines[i], lines[j] = lines[j], lines[i]
    print("Your lines: ")
    printTwoDimentionalArray(lines)
