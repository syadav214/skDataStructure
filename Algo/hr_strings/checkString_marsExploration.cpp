#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int marsExploration(string s)
{
    int count = 0;
    for (int i = 0; i < s.size();)
    {
        cout << "i: " << i << endl;
        if (s[i] != 'S')
        {
            count++;
        }

        if (s[i + 1] != 'O')
        {
            count++;
        }

        if (s[i + 2] != 'S')
        {
            count++;
        }

        i += 3;
    }
    return count;
}

int main()
{
    string s = "SOSSPSSQSSOR";
    cout << "Ans: " << marsExploration(s);
    return 0;
}
