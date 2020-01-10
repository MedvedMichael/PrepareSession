import random


def generateMatrix():  # create matrix mxn
    m, n = list(map(int, input("Input m,n: ").split()))  # m - rows, n - columns
    matrix = [[(random.uniform(-100, 100)) for j in range(0, n)] for i in range(0, m)]
    return matrix


def findMaxsAndMoveColumns(matrix):
    maxValues = []
    for i in range(0, len(matrix[0])):  # find maximums from each column
        maximum = matrix[0][i]
        for j in range(1, len(matrix)):
            if maximum < matrix[j][i]:
                maximum = matrix[j][i]
        maxValues.append(maximum)
    print("Max values: ", maxValues)
    print()

    for i in range(0, len(maxValues) - 1):  # move columns by sorting array "maxValues"
        for j in range(i + 1, len(maxValues)):
            if maxValues[i] > maxValues[j]:
                maxValues[i], maxValues[j] = maxValues[j], maxValues[i]
                moveColumns(matrix, i, j)
    print("Max values: ", maxValues)
    print()


def printMatrix(matrix):  # print the matrix in a comfortable form
    print("Your matrix: ")
    for line in matrix:
        print(line)
    print()


def moveColumns(matrix, col1, col2):  # change positions of two columns
    for i in range(0, len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]


def getLines(matrix):  # get strings from matrix's rows
    lines = []
    for row in matrix:
        line = ""
        bigZero = 0  # number of numbers bigger then 0
        smallZero = 0  # number of numbers smaller then 0
        for element in row:
            if element >= 0:
                bigZero += 1
            else:
                smallZero += 1

            line += str(element) + " "
        line += "положительных:" + str(bigZero) + ", отрицательных: " + str(smallZero)
        lines.append(line)
    print(lines)
    return lines
