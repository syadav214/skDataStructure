/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <cstdio>

int main()
{
    int a;
    long b;
    char c;
    float d;
    double e;

    //scanf("%i %li %c %f %lf", &a, &b, &c, &d, &e);
    //printf("%i\n%li\n%c\n%.03f\n%.09lf\n", a, b, c, d, e);
    scanf("%i %li", &a, &b);
    printf("%i\n%li\n", a, b);
    return 0;
}
