/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
You will be given an array of integers and a target value. 
Determine the number of pairs of array elements that have a difference equal to a target value. 
*/
int pairs(int k, vector<int> arr)
{
    int count = 0;
    map<int, int> m;

    // sort the array to 1,2,3,4,5,6,8
    sort(arr.begin(), arr.end());

    for (int i = 0; i < arr.size(); i++)
    {
        // created map with key as val+index val and subtraction of it
        m[k + arr[i]] = 1;
        m[arr[i] - k] = 1;

        cout << arr[i] << " " << k + arr[i] << " " << arr[i] - k << endl;
        if (m.count(arr[i]))
        {
            count++;
            cout << "We got one" << endl;
        }
    }

    return count;
}

int main()
{
    vector<int> arr({1, 3, 5, 8, 6, 4, 2}); //1, 5, 3, 4, 2

    cout
        << "Ans: " << pairs(2, arr) << endl;
    return 0;
}
