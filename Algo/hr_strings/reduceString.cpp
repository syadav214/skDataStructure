#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string superReducedString(string s)
{
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == s[i + 1])
        {
            s.erase(i, 2);
            i = -1;
        }
    }

    if (s == "")
    {
        return "Empty String";
    }

    return s;
}

int main()
{
    //baab, aaabccddd
    cout << "Ans: " << superReducedString("baab") << endl;
    return 0;
}
