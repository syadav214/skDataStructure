/* Compile with c++11
g++ -std=c++11 test.cpp

In this challenge, print the array after each iteration of the insertion sort, i.e.,
whenever the next element has been inserted at its correct position.
Since the array composed of just the first element is already sorted, begin printing after placing the second element.
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void printArr(int n, vector<int> arr)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void insertionSort2(int n, vector<int> arr)
{
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
        {
            int num = arr[i];
            for (int j = 0; j < i; j++)
            {
                //cout << i << " : " << j << endl;
                if (arr[i] < arr[j])
                {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            printArr(n, arr);
        }
    }
}

int main()
{
    vector<int> arr({1, 4, 3, 5, 6, 2});
    int n = arr.size();
    insertionSort2(n, arr);
    return 0;
}
