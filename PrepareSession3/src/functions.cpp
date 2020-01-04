#include "functions.h"
using namespace std;

int getN()
{
    int n = 1;
    cin >> n;
    return n;
}

int **generateMatrix(int rows)
{

    int **matrix = new int *[rows];
    for (int i = 0; i < rows; i++)
    {
        
        matrix[i] = new int[rows];
        for (int j = 0; j < rows; j++)
            matrix[i][j] = (rand() % 100) + 1;
    }
    return matrix;
}

int getSum(int **matrix, int rows)
{
    int k=0,sum=0;
    for(int i=k;i<rows;i++)
    {
        for(int j=k;j<rows;j++)
        {
            sum+=matrix[i][j];
        }
        k++;
    }
    return sum;
}

void printMatrix(int **matrix, int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void printArifm(int a1, int a2, int a3)
{
    cout<<(a1+a2+a3)/3.0<<endl;
}