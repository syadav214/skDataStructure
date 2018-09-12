/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string caesarCipher(string s, int k)
{
    string cipher = "";
    for (int i = 0; i < s.size(); i++)
    {
        int asciiVal = (int)s[i];
        char ch;
        int mod = k % 26;
        //capital
        if (asciiVal >= 65 && asciiVal <= 90)
        {
            asciiVal = asciiVal + mod;
            if (asciiVal > 90)
            {
                asciiVal = 64 + (asciiVal - 90);
            }
        }

        //small
        if (asciiVal >= 97 && asciiVal <= 122)
        {
            asciiVal = asciiVal + mod;
            if (asciiVal > 122)
            {
                asciiVal = 96 + (asciiVal - 122);
            }
        }
        //char to string
        string s1(1, (char)asciiVal);
        cipher += s1;
    }

    return cipher;
}

int main()
{
    int k;
    cin >> k;
    string s = "z";
    cout << "Ans: " << caesarCipher(s, k);
    return 0;
}
