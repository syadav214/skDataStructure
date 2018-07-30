// Print the number of letter a's in the first n letters of infinite string

#include <iostream>
#include <vector>
#include <map>
using namespace std;

int equalizeArray(vector<int> arr)
{
    map<int, int> m;
    int max = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        m[arr[i]]++;
        if (m[arr[i]] > max)
            max = m[arr[i]];
    }

    return arr.size() - max;
}

int main()
{
    vector<int> arr(5);
    arr[0] = 3;
    arr[1] = 3;
    arr[2] = 2;
    arr[3] = 1;
    arr[4] = 3;

    cout << "Ans: " << equalizeArray(arr) << endl;
    return 0;
}
