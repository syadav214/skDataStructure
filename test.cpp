/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool comp(string i, string j)
{
    int n = i.length();
    int m = j.length();
    // If length is same
    if (n == m)
        return (i < j);

    return n < m;
}

vector<string> bigSorting(vector<string> unsorted)
{
    sort(unsorted.begin(),unsorted.end(),comp);
    return unsorted;
}

int main()
{
    vector<string> unsorted({"345", "3", "23", "1", "3"});
    cout << "Ans: " << bigSorting(unsorted)[0] << endl;
    return 0;
}
