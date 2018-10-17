/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int minimumAbsoluteDifference(vector<int> arr)
{
    int min = abs(arr[0] - arr[1]);
    // sort and then check the difference
    sort(arr.begin(), arr.end());

    for (int i = 2; i < arr.size(); i++)
    {
        int absNum = abs(arr[i] - arr[i - 1]);
        if (min > absNum)
        {
            min = absNum;
        }
    }
    return min;
}

int main()
{
    vector<int> arr({-59, -36, -13, 1, -53, -92, -2, -96, -54, 75}); //1, 5, 3, 4, 2

    cout
        << "Ans: " << minimumAbsoluteDifference(arr) << endl;
    return 0;
}
