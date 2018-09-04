/*
The first line contains an integer, t , denoting the number of test cases to analyze.
Each of the next t lines contains three space-separated integers: n, c and m. 
They represent money to spend, cost of a chocolate, and the number of wrappers he can turn in for a free chocolate. 
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int chocolateFeast(int n, int c, int m)
{
    int count = n / c;
    int currentWrapper = count;

    while (currentWrapper >= m)
    {
        currentWrapper = currentWrapper - m;
        currentWrapper++;
        count++;
    }
    return count;
}

int main()
{
    int n, c, m; //(10,2,5)  (12,4,4) (6,2,2)
    cin >> n;
    cin >> c;
    cin >> m;
    cout << "Ans: " << chocolateFeast(n, c, m) << endl;
    return 0;
}
