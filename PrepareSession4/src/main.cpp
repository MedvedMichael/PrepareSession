// Variant 6 ex. 2

#include "functions.h"

int main() {
    int n = getN();
    vector<string> mLines = getLines(n);
    for(int i=0;i<n;i++)
    {
        vector<string> mWords = getWordsFromLine(mLines[i]);
        printGrow(mWords);
    }
    return 0;
}