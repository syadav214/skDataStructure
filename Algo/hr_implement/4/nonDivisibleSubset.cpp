// Find a non divisible subset

#include <iostream>
#include <vector>
using namespace std;

int nonDivisibleSubset(int k, vector<int> S)
{
    //vector of k+1 size with Value 0
    vector<int> V(k + 1, 0);

    //iterate till size of Vector S
    for (int i = 0; i < S.size(); i++)
    {
        int rem = S[i] % k;
        V[rem] += 1;
        cout << "rem: " << rem << " V[rem]: " << V[rem] << endl;
    }

    int total = min(V[0], 1);
    cout << "total: " << total << endl;

    //checking upto multiple's half
    int upto = k / 2;
    cout << "upto: " << upto << endl;
    //if multiple is double of upto then decrease 1
    if (upto * 2 == k)
    {
        upto -= 1;
    }
    cout << "after double upto: " << upto << endl;

    for (int i = 1; i <= upto; ++i)
    {
        cout << "i: " << i << "V[i]: "
             << V[i] << "[k - i]: " << k - i << " V[k - i]: "
             << V[k - i] << endl;
        total += max(V[i], V[k - i]);
        cout << "total: " << total << endl;
    }

    //If k is even then get
    if (k % 2 == 0)
    {
        total += V[k / 2] > 0;
    }

    return total;
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
