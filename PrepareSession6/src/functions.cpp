#include "functions.h"

int getN()
{
    int n=1;
    cin>>n;
    return n;
}

int** generateMatrix(int n)
{
    srand(time(NULL));
    int** matrix = new int*[n];
    for(int i=0;i<n;i++)
    {
        matrix[i] = new int[n];
        for(int j=0;j<n;j++)
        {
            matrix[i][j] = rand()%100 + 1;
        }
    }
    return matrix;
}

void fillMatrixFibonachi(int** matrix, int n)
{
    matrix[0][0] = 1;
    matrix[0][1] = 1;
    matrix[1][0] = 1;
    for(int i=2;i<n;i++)
    {
        matrix[i][0]=matrix[i-2][0]+matrix[i-1][0];
        matrix[0][i] = matrix[0][i-2] + matrix[0][i-1];
    }

    for(int j=1;j<n;j++)
    {
        for(int i=1;i<n;i++)
        {
            if(i==1)
              matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1];
            else matrix[i][j]=matrix[i-1][j] + matrix[i-2][j];
        }
    }
}

void printMatrix(int** matrix, int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }
}