// Variant 1 ex. 1
#include "functions.h"
int main() {
    int n = getN();
    int** mainMatrix = generateMatrix(n);
    fillMatrixFibonachi(mainMatrix,n);
    printMatrix(mainMatrix,n);
}