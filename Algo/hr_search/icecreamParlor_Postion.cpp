/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> icecreamParlor(int m, vector<int> arr)
{
    vector<int> pos;
    map<int, map<int, int>> k;

    for (int i = 0; i < arr.size(); i++)
    {
        cout << (m - arr[i]) << " : " << arr[i] << endl;
        if (k.count(arr[i]))
        {
            //cout << "val: " << k[arr[i]] << endl;
            for (const auto &kv : k[arr[i]])
            {
                //cout << kv.first << " has value " << kv.second << endl;
                pos.push_back(kv.second);
            }
            pos.push_back(i + 1);
            //pos.push_back(k[arr[i]])
            //cout << "Sum: " << k[arr[i]] + arr[i] << endl;
        }
        map<int, int> poss;
        poss[arr[i]] = i + 1;
        k[(m - arr[i])] = poss;
    }
    return pos;
}

int main()
{
    vector<int> arr({1, 4, 5, 3, 2});
    icecreamParlor(4, arr);
    return 0;
}
