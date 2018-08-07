// Organizing Containers of Balls with proper swapping
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

string organizingContainers(vector<vector<int>> container)
{
    int n = container[0].size();

    vector<int> sumContainers;
    vector<int> sumTypes;

    for (const auto &c : container)
    {
        // calculate number of balls in a containers
        // get sum of the given array/list. Needs start and end with initial value
        int sum = accumulate(c.begin(), c.end(), 0);
        sumContainers.push_back(sum);
    }

    for (int i = 0; i < n; i++)
    {
        // default value
        int sum{0};
        for (int j = 0; j < n; j++)
            sum += container[j][i];
        sumTypes.push_back(sum);
    }

    // sort the vectors and compare
    sort(sumTypes.begin(), sumTypes.end());
    sort(sumContainers.begin(), sumContainers.end());

    if (sumTypes == sumContainers)
        return string("Possible");
    else
        return string("Impossible");
}

int main()
{

    int numbers[] = {10, 20, 30};
    cout << accumulate(numbers, numbers + 2, 3) << endl;
    return 0;
    int n = 2;
    vector<vector<int>> container(n);
    for (int i = 0; i < n; i++)
    {
        container[i].resize(n);

        for (int j = 0; j < n; j++)
        {
            cin >> container[i][j];
        }
    }

    cout << organizingContainers(container) << endl;

    return 0;
}
