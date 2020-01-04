#include "functions.h"

int getNumber()
{
    int n = 1;
    cin >> n;
    return n;
}

void checkNumber(string text, int number, int deltaNumber)
{
    if (number == deltaNumber)
        cout << text << endl;
    else if (number < deltaNumber)
        cout << "No way" << endl;
    else

    {
        //cout << text << endl;
        
        //1 3 9 27 81     1 7 9
        //3 8             3
        //9 14            4
        //27 32           2
        //6 18 54 162     6 8
        //11 33 99
        // no 0 5

        if (number % 10 != deltaNumber % 10 && (number + 5) % 10 != deltaNumber % 10)
        {

            if (number % 10 == 0 || number % 10 == 5)
            {
                cout << "NO WAY" << endl;
            }

            else if (number % 10 == 3 || number % 10 == 9 || number % 10 == 7)
            {
                text = "(" + text + " * 3)";
                checkNumber(text, number, deltaNumber * 3);
            }
            else if (number % 10 == 8)
            {
                if (deltaNumber == 3)
                {
                    text = "(" + text + " + 5)";
                    checkNumber(text, number, deltaNumber + 5);
                }
                else
                {
                    text = "(" + text + " * 3)";
                    checkNumber(text, number, deltaNumber * 3);
                }
            }
            else if (number % 10 == 4)
            {
                if (deltaNumber == 9)
                {
                    text = "(" + text + " + 5)";
                    checkNumber(text, number, deltaNumber + 5);
                }
                else
                {
                    text = "(" + text + " * 3)";
                    checkNumber(text, number, deltaNumber * 3);
                }
            }
            else if (number % 10 == 2)
            {
                if (deltaNumber == 27)
                {
                    text = "(" + text + " + 5)";
                    checkNumber(text, number, deltaNumber + 5);
                }
                else
                {
                    text = "(" + text + " * 3)";
                    checkNumber(text, number, deltaNumber * 3);
                }
            }

            else if (number % 10 == 8)
            {
                if (deltaNumber == 6)
                {
                    text = "(" + text + " * 3)";
                    checkNumber(text, number, deltaNumber * 3);
                }
                else
                {
                    text = "(" + text + " + 5)";
                    checkNumber(text, number, deltaNumber + 5);
                }
            }
        }
        else if (number % 10 == deltaNumber % 10 || (number + 5) % 10 == deltaNumber % 10)
        {
            text = "(" + text + " + 5)";
            checkNumber(text, number, deltaNumber + 5);
        }
    }
}