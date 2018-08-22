
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Queue[100], frontIndex = 0,
                backIndex = -1;

void push(int x)
{
    backIndex++;
    Queue[backIndex] = x;
}

void pop()
{
    Queue[frontIndex] = 0;
    frontIndex++;
}

bool IsEmpty()
{
    if (backIndex < frontIndex)
        return true;
    else
        return false;
}

int front()
{
    return Queue[frontIndex];
}

int main()
{
    cout << "isempty: " << (IsEmpty() == true ? "Yes" : "No") << endl;
    push(23);
    cout << "front: " << front() << endl;
    push(12);
    cout << "front: " << front() << endl;
    pop();
    cout << "front: " << front() << endl;
    return 0;
}
