// Description: a program that prints the immortal saying "hello world"

#include <iostream>
#include <vector>
using namespace std;

int nonDivisibleSubset(int k, vector<int> S)
{
    int count = 0;
    vector<int> V[k];

    for (int i = 0; i < S.size(); i++)
    {
        int rem = S[i] % k;
        cout << "rem:" << rem << endl;
        V[S[i] % k] = V[S[i] % k] + 1;
    }

    for (int i = 0; i < S.size(); i++)
    {
        for (int j = i + 1; j < S.size(); j++)
        {
            if ((S[i] + S[j]) % k == 0)
            {
                count++;
            }
            //cout << "i:" << S[i] << " j: " << S[j] << endl;
        }
    }

    //cout << "S[0]: " << S[0] << endl;

    return count;
}

int main()
{
    int k = 3;
    vector<int> S(4);
    S[0] = 1;
    S[1] = 7;
    S[2] = 2;
    S[3] = 4;
    cout << "Ans: " << nonDivisibleSubset(k, S) << endl;
    return 0;
}
