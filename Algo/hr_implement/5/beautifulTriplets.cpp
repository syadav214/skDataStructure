/*Erica wrote an increasing sequence of n numbers in her notebook. She considers a triplet to be beautiful if:
i < j < k
arr[j] - arr[i] = arr[k] - arr[j] == d */

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int beautifulTriplets(int d, vector<int> arr)
{
    int count = 0;
    for (int i = arr.size() - 1; i > 0; i--)
    {
        for (int j = i - 1; j >= 0; j--)
        {
            if (arr[i] - arr[j] == d)
            {
                for (int k = j - 1; k >= 0; k--)
                {
                    if (arr[j] - arr[k] == d)
                    {
                        count++;
                        cout << "yo=> " << arr[i] << "-" << arr[j] << endl;
                    }
                }
            }
        }
    }
    return count;
}

int main()
{
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(4);
    arr.push_back(5);
    arr.push_back(7);
    arr.push_back(8);
    arr.push_back(10);
    beautifulTriplets(3, arr);
    return 0;
}
