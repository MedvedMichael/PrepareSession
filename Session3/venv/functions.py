def getNamesAndScores():
    names = []
    scores = []
    lines = []
    print("Input free line to end")
    line = input("Input line: ")
    while line != "":
        lines.append(line)
        nameAndScores = line.split(":")
        names.append(nameAndScores[0])
        nameAndScores[1] = nameAndScores[1].replace(",", ".")
        scores.append(list(map(float, nameAndScores[1].split())))
        line = input("Input line: ")

    return lines, names, scores


def getDopusk():
    return float(input("Input minimal score for dopusk: "))


def findExtremumsAndPushBack(score):
    minimus = min(score)
    maximus = max(score)
    print(minimus, maximus)
    del score[score.index(minimus)]
    del score[score.index(maximus)]
    score.append(minimus)
    score.append(maximus)


def getMiddleAriphmtetic(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum / len(array)


def changeStrings1(lines, names, scores):
    middles = []
    for i in range(len(names)):
        findExtremumsAndPushBack(scores[i])
        middle = getMiddleAriphmtetic(scores[i][0:len(scores[i]) - 2])
        middles.append(middle)
        lines[i] = names[i] + ": "
        for j in range(0, len(scores[i]) - 2, 1):
            lines[i] += str(scores[i][j]) + " "
        lines[i] += "= " + str(middle)
        print(lines[i])
    print()
    return middles


def makeStringFromArray(array):
    text = ""
    for i in range(len(array)):
        text += array[i]
    return text


def changeStrings2(lines, scores):
    for i in range(0, len(lines)):
        line = list(lines[i])
        line.insert(line.index("=") - 1,
                    " (" + str(scores[i][len(scores[i]) - 2]) + " " + str(scores[i][len(scores[i]) - 1]) + ")")
        lines[i] = makeStringFromArray(line)
        print(lines[i])


def printRating(rating, extraWords=""):
    print(extraWords)
    for i in range(0, len(rating)):
        text = str(i + 1) + ". " + rating[i]
        print(text)
    print()


def makeRating(lines, middles, dopusk):
    for i in range(0, len(middles) - 1):
        for j in range(i + 1, len(middles)):
            if middles[i] < middles[j]:
                middles[i], middles[j] = middles[j], middles[i]
                lines[i], lines[j] = lines[j], lines[i]
    goodRating = []
    badRating = []
    for i in range(0, len(lines)):
        if middles[i] < dopusk:
            badRating.append(lines[i])
        else:
            goodRating.append(lines[i])
    printRating(goodRating, "Dopusk: ")
    printRating(badRating, "Nedopusk: ")
    return goodRating, badRating


def printNames(names, extraText=""):
    print(extraText)
    for name in names:
        print(name)


def sortRatingByName(rating):
    localNames = []
    for i in range(len(rating)):
        localNames.append(rating[i].split(":")[0])
    localNames.sort()
    printNames(localNames, "Sorted names of nedopushchenye: ")
