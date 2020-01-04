#include "functions.h"
using namespace std;
int getN()
{
    int n=2;
    cout<<"Input n(>=2): ";
    cin>>n;
    return n;
}

double** generateMatrix(int n){
    double** matrix = new double*[2*n];
    srand(time(NULL));
    for(int i=0;i<2*n;i++){
        matrix[i] = new double[2*n];
        for(int j=0;j<2*n;j++)
        {  
            cout<<"Input "<<i<<" "<<j<<": ";
            cin>>matrix[i][j];
        }
    }
    return matrix;
}

void findMinDots(double* line, int n)
{
    double min = sqrt(pow(line[0]-line[2],2) + pow(line[1]-line[3],2));
    int index1 = 0,index2 = 2;
    for(int i=0;i<2*n-2;i+=2)
    {
        for(int j=i+2;j<2*n;j++)
        {
            double delta = sqrt(pow(line[i]-line[j],2) + pow(line[i+1]-line[j+1],2));
            if(min>delta) {
             min = delta;
             index1 = i;
             index2 = j;
            }
        }
    }

    cout<< line[index1]<<" "<<line[index1+1]<<" "<<line[index2]<<" "<<line[index2+1]<<endl;
}

