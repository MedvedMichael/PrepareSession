import random


def getLines():
    lines = []
    print("Input free line to end input")
    line = input("Input line:")
    while line != "":
        lines.append(line)
        line = input("Input line:")
    return lines


def changeLines(lines):
    print("Your changed lines: ")
    for j in range(len(lines)):
        line = list(lines[j])
        i = 0
        counter = 1
        while i < len(line) - 1:
            if line[i] == line[i + 1] and line[i] != " ":
                del line[i]
                counter += 1

                i -= 1

            else:
                if counter != 1:
                    line.insert(i + 1, "{" + str(counter) + "}")
                    counter = 1
                    i += 1
            i += 1
            if i == len(line) - 1 and counter != 1:  # проверка на последний элемент
                line.insert(i + 1, "{" + str(counter) + "}")
                break
        lines[j] = getLineFromArray(line)
        print(lines[j])


def getLineFromArray(array):
    text = ""
    for element in array:
        text += str(element)
    return text


def getNumbersFromLines(lines):
    numbers = []
    for line in lines:
        for i in range(0, len(line)):
            if 57 >= int(ord(line[i])) >= 48:
                numbers.append(int(line[i]))
    return numbers


def generateMatrix(array):
    matrix = [[0 for i in range(len(array))] for j in range(len(array))]
    for i in range(len(array)):
        matrix[i][i] = array[i]

    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j] = random.randint(0, array[0])
            matrix[j][i] = random.randint(0, array[-1])

    printMatrix(matrix, "Your start matrix is: ")
    return matrix


def printMatrix(matrix, extraText=""):
    print(extraText)
    for row in matrix:
        print(row)
    print()


def getRowIndexOfMaxColumnElement(matrix):
    columnIndex = int(input("Input column index: "))
    maximus = matrix[0][columnIndex]
    rowIndex = 0
    for j in range(1, len(matrix)):
        if matrix[j][columnIndex] >= maximus:
            maximus = matrix[j][columnIndex]
            rowIndex = j

    return rowIndex


def removeRow(matrix, rowIndex):
    del matrix[rowIndex]
    printMatrix(matrix, "Matrix after cutting: ")
