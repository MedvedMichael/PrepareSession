// Variant 3 ex. 1

#include "functions.h"
int main() {
    srand(time(NULL));
    int n = getN();
    int** arrOfMatrixs [3];
    int sums[3];
    for(int i=0;i<3;i++)
    {
        arrOfMatrixs[i] = generateMatrix(n);
        printMatrix(arrOfMatrixs[i],n);
        sums[i] = getSum(arrOfMatrixs[i],n);
    }

    printArifm(sums[0],sums[1],sums[2]);

}
   