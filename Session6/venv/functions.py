import random


def generateMatrix():
    n = int(input("Input n: "))
    matrix = [[random.randint(-100, 100) for j in range(n)] for i in range(n)]
    printMatrix(matrix)
    return matrix


def printMatrix(matrix):
    for line in matrix:
        print(line)
    print()


def getRombArray(matrix):
    array = []
    if len(matrix) % 2 == 1:
        start = int(len(matrix) / 2)
        finish = start
    else:
        finish = int(len(matrix) / 2)
        start = finish - 1
    itter = 0
    while start >= 0:
        for i in range(start, finish + 1):
            array.append(matrix[itter][i])
            if itter != len(matrix) - itter - 1:
                array.append(matrix[len(matrix) - itter - 1][i])
        start -= 1
        finish += 1
        itter += 1
    print(array)
    return array
