#include <iostream>
#include <bits/stdc++.h>
using namespace std;
ifstream f("data.in");
ofstream g("data.out");

int A[100], n, i;

int main()
{
    f >> n;
    //cout << n << endl;
    for (i = 1; i < n; ++i)
    {
        int x;
        f >> x;
        //cout << x << endl;
        //x = x + 10;
        ++A[x];
        cout << x << " == " << A[x] << endl;
    }

    if (A[1] > 0)
        g << "YES, it appears";
    else
        g << "NO, it's not";

    return 0;
}
