#Variant 15 ex. 1
import functions

listOfMatrix = [[], []]
listOfMatrix[0], listOfMatrix[1] = functions.createMatrix(), functions.createMatrix()
functions.printMatrixs(listOfMatrix)
functions.findMaxUnderDiagAndDel(listOfMatrix)
functions.printMatrixs(listOfMatrix)
