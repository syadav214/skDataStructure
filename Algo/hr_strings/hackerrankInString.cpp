#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string hackerrankInString(string s)
{
    string hs = "hackerrank";
    int i = 0;

    for (int j = 0; j < s.size(); j++)
    {
        if (s[j] == hs[i])
        {
            i++;
        }
    }

    if (i == 10)
    {
        return "YES";
    }
    else
    {
        return "NO";
    }
}

int main()
{
    string s = "hackerworld";
    cout << "Ans: " << hackerrankInString(s);
    return 0;
}
