#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int minimumNumber(int n, string password)
{
    bool numbers = false, lowercase = false, uppercase = false, speacialChar = false;
    // 48 to 57
    // 65 to 90
    // 97 to 122
    for (int i = 0; i < n; i++)
    {
        int asciiVal = (int)password[i];
        if (asciiVal >= 48 && asciiVal <= 57)
        {
            numbers = true;
        }
        else if (asciiVal >= 65 && asciiVal <= 90)
        {
            uppercase = true;
        }
        else if (asciiVal >= 97 && asciiVal <= 122)
        {
            lowercase = true;
        }
        else
        {
            speacialChar = true;
        }
    }

    int cnt = 0;
    if (numbers)
    {
        cnt++;
    }

    if (lowercase)
    {
        cnt++;
    }

    if (uppercase)
    {
        cnt++;
    }

    if (speacialChar)
    {
        cnt++;
    }

    cout << numbers << " " << lowercase << " " << uppercase << " " << speacialChar << endl;
    int diff = 4 - cnt;
    cout << diff;

    if (n > 5)
    {
        return diff;
    }
    else
    {
        int diffFromSix = (6 - (n + diff));
        if (diffFromSix < 0)
        {
            return diff;
        }
        return diff + diffFromSix;
        // return 6 - cnt;
    }
}

int main()
{
    //#HackerRank Ab1 E!%Z@
    string s = "Ab1";
    int n = s.size();
    cout << "Ans: " << minimumNumber(n, s) << endl;
    return 0;
}
