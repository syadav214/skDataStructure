// Print the number of letter a's in the first n letters of infinite string

#include <iostream>
#include <vector>
using namespace std;

long repeatedString(string s, long n)
{
    long loops = (n / s.length());
    long remainder = (n % s.length());
    long cnt = 0, extra_a = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == 'a')
        {
            cnt++;
            if (i < remainder)
            {
                extra_a++;
            }
        }
    }

    cnt = (loops * cnt) + extra_a;

    return cnt;
}

int main()
{
    string s = "aba";
    long n = 10;
    cout << "Ans: " << repeatedString(s, n) << endl;
    return 0;
}
