#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void printVect(int n, vector<int> arr)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// We have to move last element of the array to its sorted position
void insertionSort1(int n, vector<int> arr)
{
    int v = arr[n - 1];
    for (int i = n - 2; i > -1; i--)
    {
        cout << "v: " << v << " i:" << i << endl;
        if (v < arr[i])
        {
            cout << "1st\n";
            arr[i + 1] = arr[i];
            printVect(n, arr);
            if (i == 0)
            {
                arr[i] = v;
                printVect(n, arr);
            }
        }
        else
        {
            cout << "2nd\n";
            arr[i + 1] = v;
            printVect(n, arr);
            break;
        }
    }
}

int main()
{
    vector<int> arr({2, 4, 6, 8, 1});
    insertionSort1(5, arr);
    return 0;
}
