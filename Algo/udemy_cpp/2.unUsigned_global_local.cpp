// Check value of global and local variable
#include <iostream>
using namespace std;

// global will have a fixed value
int a[3];

int main()
{
    // local will keep changing its value
    int a1[3];

    cout << a << endl
         << a1;

    return 0;
}
