// Variant 2 ex. 1
#include "functions.h"

int main()
{
    int *arr = getVariables();
    int m = arr[0], n = arr[1], k = arr[2];
    int **mainMatrix = generateMatrix(m, n);
    int *maxPosition = findMaxElementPosition(mainMatrix, m, n);

    printMatrix(mainMatrix, m, n);
    replaceRowsAndColumns(mainMatrix, maxPosition, m, n, k);

    printMatrix(mainMatrix, m, n);
}