/*We define the distance between two array values as the number of indices between the two values. 
Given , find the minimum distance between any pair of equal elements in the array.
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int minimumDistances(vector<int> a)
{
    int k = 0, c = -1;
    int b[a.size()];

    for (int i = 0; i < a.size(); i++)
    {
        for (int j = i + 1; j < a.size(); j++)
        {
            if (a[i] == a[j])
            {
                c = i - j;
                if (c < 0)
                    c = -1 * c;
                b[k] = c;
                k++;
            }
        }
    }

    int min = b[0];
    if (c == -1)
        min = c;
    else
    {
        for (int i = 0; i < k; i++)
        {
            if (b[i] < min)
                min = b[i];
        }
    }

    return min;
}

int main()
{
    vector<int> a;
    a.push_back(7);
    a.push_back(1);
    a.push_back(3);
    a.push_back(4);
    a.push_back(1);
    a.push_back(7);
    cout << "Ans: " << minimumDistances(a) << endl;
    return 0;
}
