#include <iostream>
using namespace std;

int taumBday(int b, int w, int bc, int wc, int z)
{
    if (bc + z < wc)
    {
        return (bc * b + w * (bc + z));
    }
    else if (wc + z < bc)
    {
        return (wc * w + b * (wc + z));
    }
    else
    {
        return (bc * b + wc * w);
    }
}

int main()
{
    int b = 7, w = 7, bc = 4, wc = 2, z = 1;
    //int b = 3, w = 6, bc = 9, wc = 1, z = 1;
    cout << "Ans: " << taumBday(b, w, bc, wc, z) << endl;

    return 0;
}
