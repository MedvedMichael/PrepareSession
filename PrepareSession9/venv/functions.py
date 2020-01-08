import random
import copy


def createMatrix():
    m, n = list(map(int, input("Input m,n: ").split()))
    matrix = [[int(random.random() * 100 + 1) for j in range(0, n)] for i in range(0, m)]
    return matrix


def findExtremums(matrix):
    lastMatrix = copy.deepcopy(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            flag = 1
            if i != 0 and lastMatrix[i][j] < lastMatrix[i - 1][j]:
                flag = 0
            if i != len(lastMatrix) - 1 and lastMatrix[i][j] < lastMatrix[i + 1][j]:
                flag = 0
            if j != 0 and lastMatrix[i][j] < lastMatrix[i][j - 1]:
                flag = 0
            if j != len(lastMatrix[0]) - 1 and lastMatrix[i][j] < lastMatrix[i][j + 1]:
                flag = 0
            if flag:
                matrix[i][j] = -matrix[i][j]

    printMatrix(lastMatrix)
    print()
    printMatrix(matrix)


def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])
