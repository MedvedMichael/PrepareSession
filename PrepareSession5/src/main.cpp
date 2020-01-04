// Variant 6 ex. 1

#include "functions.h"

int main() {
    int n = getN();
    double** mainMatrix = generateMatrix(n);
    for(int i=0;i<2*n;i++)
    {
        findMinDots(mainMatrix[i],n);
    }
}