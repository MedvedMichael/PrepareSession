import math


def convert16to10(num16=""):
    num10 = 0
    alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for i in range(len(arr16)):
        num10 += (16 ** (len(num16) - i - 1)) * alphabet.index(num16[i])
    print(num10)
    return num10


def convert10to16(num10=0):
    arr = []
    alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while num10 >= 16:
        arr.insert(0, alphabet[num10 % 16])
        num10 //= 16
    if num10 != 0:
        arr.insert(0, alphabet[num10])
    text = ""
    for element in arr:
        text += str(element)
    print(text)
    return text


def convert10to2(num10=0):
    arr = []
    while num10 >= 2:
        arr.insert(0, num10 % 2)
        num10 //= 2
    if num10 == 1:
        arr.insert(0, 1)
    text = ""
    for element in arr:
        text += str(element)

    return text


def convert2to10(num2=""):
    num10 = 0
    for i in range(len(num2)):
        num10 += 2 ** (len(num2) - i - 1) * int(num2[i])

    return num10


def convert16to2(num16=""):
    alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    num2 = ""
    for i in range(len(num16)):
        element = alphabet.index(num16[i])
        deltaNum = convert10to2(element)
        while len(deltaNum) < 4:
            deltaNum = "0" + deltaNum
        num2 += str(int(deltaNum))
    print(num2)
    return num2


def convert2to16(num2=""):
    alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    num16 = ""
    while len(num2) % 4 != 0:
        num2 = "0" + num2
    for i in range(0, len(num2), 4):
        deltaNum = alphabet[convert2to10(num2[i:i + 4])]
        num16 += deltaNum
    print(num16)
