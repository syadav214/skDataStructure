#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> missingNumbers(vector<int> arr, vector<int> brr)
{
    vector<int> mNos;
    map<int, int> m;
    map<int, int> n;

    for (int i = 0; i < brr.size(); i++)
    {
        m[brr[i]]++;
    }

    for (int i = 0; i < arr.size(); i++)
    {
        n[arr[i]]++;
    }

    for (const auto &kv : m)
    {
        if (n[kv.first] != kv.second)
        {
            mNos.push_back(kv.first);
        }
    }

    return mNos;
}

int main()
{
    vector<int>
        arr({203, 204, 205, 206, 207, 208, 203, 204, 205, 206});

    vector<int>
        brr({203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204});

    missingNumbers(arr, brr);
    return 0;
}
