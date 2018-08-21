
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Stack[100], ind = 0;

void push(int x)
{
    ++ind;
    Stack[ind] = x;
}

void pop()
{
    Stack[ind] = 0;
    --ind;
}

bool IsEmpty()
{
    if (ind > 0)
        return false;
    else
        return true;
}

int top()
{
    return Stack[ind];
}

int main()
{
    //ind = 0;
    push(1);
    push(5);

    if (!IsEmpty())
    {
        cout << top() << endl;
    }

    pop();

    if (!IsEmpty())
    {
        cout << top() << endl;

        return 0;
    }
}
