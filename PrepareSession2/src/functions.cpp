#include "functions.h"
using namespace std;

int *getVariables()
{
    int arr[] = {1, 1, 0};
    cin >> arr[0] >> arr[1] >> arr[2];
    int *p = arr;
    return p;
}

int **generateMatrix(int rows, int columns)
{
    srand(time(NULL));
    int **matrix = new int *[rows];
    for (int i = 0; i < rows; i++)
    {
        matrix[i] = new int[columns];
        for (int j = 0; j < columns; j++)
            matrix[i][j] = rand() % 100 + 1;
    }
    return matrix;
}

int *findMaxElementPosition(int **matrix, int rows, int columns)
{
    int max = matrix[0][0];
    int position[] = {0, 0};
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (max < matrix[i][j])
            {
                max = matrix[i][j];
                position[0] = i;
                position[1] = j;
            }
        }
    }

    int *p = new int[2]{position[0], position[1]};
    return p;
}

void replaceRowsAndColumns(int **matrix, int *position, int rows, int columns, int k)
{
    for (int i = 0; i < rows; i++)
    {
        int delta = matrix[i][position[1]];
        matrix[i][position[1]] = matrix[i][k];
        matrix[i][k] = delta;
    }

    for (int i = 0; i < columns; i++)
    {
        int delta = matrix[position[0]][i];
        matrix[position[0]][i] = matrix[k][i];
        matrix[k][i] = delta;
    }
}

void printMatrix(int **matrix, int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout<<endl;
}