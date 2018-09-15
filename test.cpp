/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string pangrams(string s)
{
    // convert to lower. we can do upper using ::toupper
    transform(s.begin(), s.end(), s.begin(), ::tolower); 
    map<char, int> m;

    for (int i = 0; i < s.size(); i++)
    {
        if (m.count(s[i]) == false)
        {
            m[s[i]] = 1;
        }
    }

    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    bool allFound = true;

    for (int i = 0; i < alphabet.size(); i++)
    {
        if (m.count(alphabet[i]) == false)
        {
            allFound=false;
            break;
        }
    }
    
    if(allFound)
    {
        return "pangram";    
    }

    return "not pangram";
}

int main()
{
    string s = "We promptly judged antique ivory buckles for the next prize";
    cout << "Ans: " << pangrams(s) << endl;
    return 0;
}
