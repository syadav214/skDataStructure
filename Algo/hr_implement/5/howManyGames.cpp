/*
You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars. 
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price.
Specifically, the first game you buy during the sale will be sold at p dollars, 
but every subsequent game you buy will be sold at exactly d dollars less than the cost of the previous one you bought.
This will continue until the cost becomes less than or equal to m dollars, after which every game you buy will cost m dollars each.
*/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int howManyGames(int p, int d, int m, int s)
{
    if (s < p)
        return 0;
    if (s == p)
        return 1;
    int count = 1;
    int sum = p;
    while (p - d >= m)
    {
        p = p - d;
        if (sum + p > s)
            return count;
        else
            count++;
        sum += p;
    }
    p = m;
    while (sum + p <= s)
    {
        sum = sum + p;
        count++;
    }
    return count;
}

int main()
{
    cout << "Ans: " << howManyGames(20, 3, 6, 80) << endl;
    return 0;
}
