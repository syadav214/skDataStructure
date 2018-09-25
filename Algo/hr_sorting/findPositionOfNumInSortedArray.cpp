#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int introTutorial(int V, vector<int> arr)
{
    int pos = 0;
    int arrL = arr.size();
    int left = 0;
    int right = arrL - 1;

    while (left <= right)
    {
        int mid = 0;
        if (arrL % 2 == 0)
        {
            mid = (left + right + 1) / 2;
        }
        else
        {
            mid = left + right / 2;
        }
        cout << "left: " << left << " right:" << right << " mid:" << mid << endl;
        cout << "arr[mid]: " << arr[mid] << endl;
        if (arr[mid] == V)
        {
            pos = mid;
            break;
        }
        else if (arr[mid] > V)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
        cout << "left: " << left << " right:" << right << " mid:" << mid << endl;
        cout << "======================================" << endl;
    }

    return pos;
}

int main()
{
    vector<int> arr({1, 4, 5, 7, 9, 12});
    cout << "Ans: " << introTutorial(4, arr) << endl;
    return 0;
}
