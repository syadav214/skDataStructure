// Kaprekar number example => If n=9, and n2=81. This gives us 1+8 = 9 , the original number.

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> kaprekarNumbers(int p, int q)
{
    int reminder_of_square, divided_value;
    long int sq;
    int len;
    vector<int> kkNumbers;
    for (int i = p; i <= q; i++)
    {
        sq = (long int)i * i;
        // To find length of integer use log10 and add 1 to it
        len = (int)log10(i) + 1;
        reminder_of_square = sq % (int)pow(10, len);
        divided_value = sq / (int)pow(10, len);
        if (reminder_of_square + divided_value == i)
            kkNumbers.push_back(i);
    }
    return kkNumbers;
}

int main()
{
    kaprekarNumbers(1, 100);
    return 0;
}
