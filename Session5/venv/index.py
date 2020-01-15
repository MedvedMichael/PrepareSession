import functions

# главная матрица
mainMatrix = functions.generateMatrix()

# положение максимального элемента матрицы
mMaxIndex = functions.findMaxElement(mainMatrix)
functions.changeRowsAndColumns(mainMatrix,mMaxIndex)

# строки полученые из матрицы змейкой
mLines = functions.getArrayOfStrings(mainMatrix)
functions.invertLinesFromArray(mLines)

functions.deleteFloatPartFromLines(mLines)