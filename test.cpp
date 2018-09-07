/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int camelcase(string s)
{
    int count = 1;

    for (int i = 0; i < s.size(); i++)
    {
        int asciiVal = (int)s[i];
        if (asciiVal >= 65 && asciiVal <= 90)
        {
            count++;
        }
    }

    return count;
}

int main()
{
    cout << "Ans: " << camelcase("saveChangesInTheEditor") << endl;
    return 0;
}
