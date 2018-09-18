#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string funnyString(string s)
{
    int j = s.size() - 1;
    for (int i = 1; i < s.size(); i++)
    {
        int primary1Char = (int)s[i];
        int primary2Char = (int)s[i - 1];

        int secondary1Char = (int)s[j - 1];
        int secondary2Char = (int)s[j];

        int diffPri = primary1Char - primary2Char;
        if (diffPri < 0)
        {
            diffPri *= -1;
        }

        int diffSec = secondary1Char - secondary2Char;
        if (diffSec < 0)
        {
            diffSec *= -1;
        }

        if (diffPri != diffSec)
        {
            return "Not Funny";
        }

        j--;
    }

    return "Funny";
}

int main()
{
    string s = "acxz";
    cout << "Ans: " << funnyString(s) << endl;
    return 0;
}
