import random


def createMatrix():
    n = int(input("Input n: "))
    matrix = [[int(random.random() * 100 + 1) for j in range(0, n)] for i in range(0, n)]
    return matrix


def printMatrixs(listOfMatrix):
    for j in listOfMatrix:
        for i in j:
            print(i)
        print()
    print()


def findMaxUnderDiagAndDel(matrixs):
    for matrix in matrixs:
        max = matrix[1][0]
        maxPosition = [1, 0]
        for i in range(2, len(matrix)):
            for j in range(0, i):
                if max < matrix[i][j]:
                    max = matrix[i][j]
                    maxPosition = [i, j]
        del matrix[maxPosition[0]]
        for i in matrix:
            del i[maxPosition[1]]
