import random


def createArray():
    n = int(input("Input n: "))
    arr = [int(random.random() * 100 + 1) for i in range(0, n)]
    return arr


def createMatrix(arr):
    matrix = [[0 for i in range(0, len(arr))] for j in range(0, len(arr))]
    for i in range(0, len(arr)):
        for j in range(0, i + 1):
            matrix[i - j][j] = arr[i]

    for i in range(1, len(arr)):
        for j in range(len(arr) - 1, i - 1, -1):
            matrix[len(arr) - 1 - j + i][j] = arr[i - 1]
    return matrix


def deleteRowAndColumn(matrix):
    k = int(input("Input k: "))
    del matrix[k]
    for i in matrix:
        del i[k]


def printMatrix(matrix):
    for i in matrix:
        print(i)
