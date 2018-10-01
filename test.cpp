/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// make left (less than 1st element), equal and right (greater than 1st element) arrays
vector<int> quickSort(vector<int> arr)
{
    vector<int> right;
    vector<int> finalArr;

    for (int i = 1; i < arr.size(); i++)
    {
        if (arr[i] < arr[0])
        {
            finalArr.push_back(arr[i]);
        }
        else
        {
            right.push_back(arr[i]);
        }
    }

    finalArr.push_back(arr[0]);

    for (int i = 0; i < right.size(); i++)
    {
        finalArr.push_back(right[i]);
    }
    return finalArr;
}

int main()
{
    vector<int> arr({4, 5, 3, 7, 2});
    quickSort(arr);
    return 0;
}
