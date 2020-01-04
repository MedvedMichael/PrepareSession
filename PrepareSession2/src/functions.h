#include <iostream>
#include <time.h>

int** generateMatrix(int,int);
int* getVariables();
int* findMaxElementPosition(int**,int,int);
void replaceRowsAndColumns(int**,int*,int,int,int);
void printMatrix(int**,int,int);
