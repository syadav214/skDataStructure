
#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<int, int> m;
    for (int i = 0; i < 5; i++)
    {
        m[i]++;
    }

    cout << "Ans: " << m[2] << endl;
    return 0;
}
