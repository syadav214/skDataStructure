// Print the number of letter a's in the first n letters of infinite string

#include <iostream>
#include <vector>
using namespace std;

int jumpingOnClouds(vector<int> c)
{
    int steps = 0;
    for (int i = 0; i < c.size(); i++)
    {
        if (i == (c.size() - 1))
            break;

        // increase the i if found zero on i+2
        if (((i + 2) < c.size() && c[i + 2] == 0))
            i++;

        steps++;
    }

    return steps;
}

int main()
{
    vector<int> c(7);
    c[0] = 0;
    c[1] = 0;
    c[2] = 1;
    c[3] = 0;
    c[4] = 0;
    c[5] = 1;
    c[6] = 0;
    /*vector<int> c(6);
    c[0] = 0;
    c[1] = 0;
    c[2] = 0;
    c[3] = 1;
    c[4] = 0;
    c[5] = 0;*/

    cout << "Ans: " << jumpingOnClouds(c) << endl;
    return 0;
}
