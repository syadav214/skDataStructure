// encrypting a string with few rules
#include <iostream>
#include <cmath>
using namespace std;

string encryption(string s)
{
    double sqrt_s = sqrt(s.length());
    int ceil_s = ceil(sqrt_s);
    int floor_s = floor(sqrt_s);
    cout << ceil_s << " " << floor_s << endl;
    string result = "";
    if ((ceil_s * floor_s) < s.length())
    {
        floor_s = ceil_s;
    }

    cout << ceil_s << " " << floor_s << endl;

    for (int i = 0; i < ceil_s; i++)
    {
        int x = i;
        for (int j = 0; j < floor_s; j++)
        {
            if (x < s.length())
            {
                result += s[x];
                x += ceil_s;
            }
        }
        if (i < ceil_s - 1)
            result += " ";
    }
    return result;
}

int main()
{
    //cout << encryption("haveaniceday") << endl;
    cout << encryption("chillout") << endl;
    return 0;
}
