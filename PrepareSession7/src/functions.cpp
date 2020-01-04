#include "functions.h"
string getLine()
{
    string line="";
    getline(cin,line);
    return line;
}

vector<string> getBinaryNumbers(string line)
{
    vector<string> tokens;
    string token;
    istringstream tokenStream(line);
    while(getline(tokenStream,token,' '))
    {
        if(!token.empty())
          tokens.push_back(token);
    }
    return tokens;
}


void printMiddleAriphmetic(vector<string> binNumbers)
{
    int sum = 0;
    for(int i=0;i<binNumbers.size();i++)
    {
        sum+=getNumberFromBinary(binNumbers[i]);
    }
    cout<<sum*1.0/binNumbers.size()<<endl;
}

int getNumberFromBinary(string binNumber)
{
    int sum = 0;
    for(int i=0;i<binNumber.length();i++)
    {
        if(binNumber[i]=='1')
         sum+=pow(2,binNumber.length()-i-1);
    }
    return sum;
}
