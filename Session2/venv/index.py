# Variant from Михаил Косюк
import functions

mainMatrix = functions.generateMatrix()
functions.mirrorMatrix(mainMatrix)
functions.deleteColumn(mainMatrix)

mLines = functions.generateLines(mainMatrix)

functions.sortArrayOfLines(mLines)



