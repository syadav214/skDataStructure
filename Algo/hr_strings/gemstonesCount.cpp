#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int gemstones(vector<string> arr)
{
    int count = 0;
    map<char, int> m;

    for (int i = 0; i < arr.size(); i++)
    {
        bool insideLoop = false;
        string s = arr[i];
        map<char, int> mInside;
        for (int j = 0; j < s.size(); j++)
        {
            mInside[s[j]]++;
            // We will increment count only once for a string
            if (mInside[s[j]] == 1)
            {
                m[s[j]]++;
                if (m[s[j]] == arr.size())
                {
                    count++;
                }
                //cout << "ch: " << s[j] << " vl:" << m[s[j]] << endl;
            }
        }
    }

    return count;
}

int main()
{
    vector<string> arr;
    arr.push_back("abcdde");
    arr.push_back("baccd");
    arr.push_back("eeabg");
    cout << "Ans: " << gemstones(arr) << endl;
    return 0;
}
