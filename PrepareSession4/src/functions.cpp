#include "functions.h"

int getN()
{
    int n=1;
    string s;
    getline(cin,s);
    n = stoi(s);
    return n;
}

vector<string> getLines(int n)
{
    vector<string> lines;
    string line="";
    for(int i=0;i<n;i++)
    {
        getline(cin,line);
        lines.push_back(line);
    }
    return lines;
}

vector<string> getWordsFromLine(string line)
{
    vector<std::string> tokens;
    string token;
    istringstream tokenStream(line);
    while (getline(tokenStream, token, ' '))
    {
        if(!token.empty())
       tokens.push_back(token);
    }
    return tokens;
}

void printGrow(vector<string> words)
{
    if(words.size()!=0){
     int min = words[0].length();
     int indexMin = 0;
     for(int i=1;i<words.size();i++)
     {
        if(min>words[i].length())
        {
           min=words[i].length();
           indexMin = i;
        }
     }
     cout<<words[indexMin]<<" ";
     words.erase(words.begin()+indexMin);
    }
    if(words.size()!=0)
       printGrow(words);
    else cout<<endl;

}