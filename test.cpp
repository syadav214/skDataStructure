#include <iostream>
#include <vector>

using namespace std;

int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles)
{
}

int main()
{
    int n = 5, k = 3, r_q = 4, c_q = 3;

    vector<vector<int>> obstacles(k);
    for (int i = 0; i < k; i++)
    {
        obstacles[i].resize(2);

        for (int j = 0; j < 2; j++)
        {
            cin >> obstacles[i][j];
        }
    }

    cout << "Ans: " << queensAttack(n, k, r_q, c_q, obstacles);
    return 0;
}
