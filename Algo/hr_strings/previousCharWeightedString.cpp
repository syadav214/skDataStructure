// if same char repeats then add the weight of it and push to vector

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<string> weightedUniformStrings(string s, vector<int> queries)
{
    vector<string> result;
    map<int, int> m;
    string prevConStr = "";

    for (int i = 0; i < s.size(); i++)
    {
        int charVal = (int)s[i] - 96;
        if (i > 0)
        {
            if (s[i] == s[i - 1])
            {
                if (prevConStr == "")
                {
                    prevConStr = s[i - 1];
                }
                string s1(1, s[i]);
                prevConStr += s1;
                charVal = charVal * prevConStr.size();
            }
            else
            {
                prevConStr = "";
            }
        }
        //cout << s[i] << " : " << charVal << endl;
        m.insert({charVal, 1});
    }

    for (int i = 0; i < queries.size(); i++)
    {
        if (m.count(queries[i]))
        {
            result.push_back("Yes");
        }
        else
        {
            result.push_back("No");
        }
    }

    return result;
}

int main()
{
    string s = "abccddde";
    vector<int> queries;
    queries.push_back(1);
    queries.push_back(3);
    queries.push_back(12);
    queries.push_back(5);
    queries.push_back(9);
    queries.push_back(10);

    vector<string> val = weightedUniformStrings(s, queries);
    cout << "Ans: " << val[0] << endl;
    return 0;
}
