/*
Taum is planning to celebrate the birthday of his friend, Diksha. 
There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
 To make her happy, Taum has to buy black gifts and white gifts.

    The cost of each black gift is units.
    The cost of every white gift is units.
    The cost of converting each black gift into white gift or vice versa is units.
*/

#include <iostream>
using namespace std;

int taumBday(int b, int w, int bc, int wc, int z)
{
    //if cost of black and conversion is less than white then
    if (bc + z < wc)
    {
        return ((bc * b) + (w * (bc + z)));
    }
    //if cost of white and conversion is less than black then
    else if (wc + z < bc)
    {
        return ((wc * w) + (b * (wc + z)));
    }
    else
    {
        return ((bc * b) + (wc * w));
    }
}

int main()
{
    int b = 7, w = 7, bc = 4, wc = 2, z = 1;
    //int b = 3, w = 6, bc = 9, wc = 1, z = 1;
    cout << "Ans: " << taumBday(b, w, bc, wc, z) << endl;

    return 0;
}
