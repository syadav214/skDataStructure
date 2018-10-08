/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
Lauren has a chart of distinct projected prices for a house over the next several years. 
She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.
*/
int minimumLoss(vector<long> price)
{
    map<long, int> m;

    for (int i = 0; i < price.size(); i++)
    {
        m[price[i]] = i;
    }

    sort(price.begin(), price.end());

    long minimumLoss = LONG_MAX;

    //Iterate from end to start
    for (int i = price.size() - 1; i > 0; i--)
    {
        //Make sure it is a smaller loss
        if ((price[i] - price[i - 1]) < minimumLoss)
        {
            //Verify if the pair is a valid transaction
            if (m[price[i]] < m[price[i - 1]])
            {
                minimumLoss = (price[i] - price[i - 1]);
            }
        }
    }

    return minimumLoss;
}

int main()
{
    vector<long>
        arr({20, 7, 8, 2, 5});
    cout << "Ans: " << minimumLoss(arr) << endl;
    return 0;
}

/*O(n2) Solution

int minimumLoss(vector<long> price)
{
    long minLoss = LONG_MAX;

    for (int i = 0; i < price.size(); i++)
    {
        for (int j = i + 1; j < price.size(); j++)
        {
            int diff = price[i] - price[j];
            if (diff > 0 && minLoss > diff)
            {
                minLoss = diff;
            }
        }
    }

    return minLoss;
}


*/
