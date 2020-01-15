import random
import math


# создает матрицу nxm
def generateMatrix():
    n = int(input("Input number of rows: "))
    m = int(input("Input number of columns: "))
    matrix = [[round(random.uniform(-100, 100), 3) for j in range(m)] for i in range(n)]
    printMatrix(matrix, "Start matrix: ")
    return matrix


# находит максимальный элемент и возвращает его положение
def findMaxElement(matrix):
    maximus = matrix[0][0]
    maxIndex = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if maximus < matrix[i][j]:
                maximus = matrix[i][j]
                maxIndex = [i, j]
    print("Max element = " + str(maximus) + " on position " + str(maxIndex[0]) + ", " + str(maxIndex[1]))
    return maxIndex


# выводит матрицу
def printMatrix(matrix, extraText=""):
    print(extraText)
    for row in matrix:
        print(row)
    print()


# выводит все строки
def printLines(lines, extraText=""):
    print(extraText)
    for line in lines:
        print(line)
    print()


# меняет строки и столбцы так, чтобы макс. элемент был на месте [k,k]
def changeRowsAndColumns(matrix, maxIndex):
    k = int(input("Input k: "))
    matrix[maxIndex[0]], matrix[k] = matrix[k], matrix[maxIndex[0]]
    for i in range(len(matrix)):
        matrix[i][maxIndex[1]], matrix[i][k] = matrix[i][k], matrix[i][maxIndex[1]]
    printMatrix(matrix, "Matrix after changing: ")


# возвращает массив строчек полученых из строчек матрицы змейкой
def getArrayOfStrings(matrix):
    lines = []
    for i in range(len(matrix)):
        lines.append(getLineFromArray(matrix[i], i))
    printLines(lines, "Start lines: ")
    return lines


# возвращает строчку созданную из элементов массива через пробел (направление зависит от индекса)
def getLineFromArray(array, index=0):
    text = ""
    if index % 2 == 0:
        for element in array:
            text += str(element) + " "
    else:
        for i in range(len(array) - 1, -1, -1):
            text += str(array[i]) + " "
    return text


# инвертирует положение всех чисел в строках массива
def invertLinesFromArray(lines):
    for i in range(len(lines)):
        lines[i] = invertLine(lines[i])
    printLines(lines, "Lines after invert: ")


# инвертирует положение элементов в массиве
def invertLine(line):
    array = list(map(float, line.split()))
    array.reverse()
    line = getLineFromArray(array)
    return line


# удаляет дробную часть у всех элементов строк массива
def deleteFloatPartFromLines(lines):
    for i in range(len(lines)):
        lines[i] = floatToIntInString(lines[i])
    printLines(lines, "Lines after converting elements to int: ")


# удаляет дробную часть у всех элементов строки
def floatToIntInString(line):
    array = list(map(float, line.split()))
    for i in range(len(array)):
        array[i] = int(array[i])
    line = getLineFromArray(array)
    return line
