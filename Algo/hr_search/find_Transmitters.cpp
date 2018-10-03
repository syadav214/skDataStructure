/* Compile with c++11
g++ -std=c++11 test.cpp
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int hackerlandRadioTransmitters(vector<int> ar, int k) 
{
    sort(ar.begin(),ar.end());

    int i=0,j=0,n=ar.size(),c=0,x=0;
    while(i<n)
    {
        j=i+1;
        while((ar[i]+k>=ar[j])&&(j<n))
        {
            j+=1;
        }
        x=j;
        j-=1;
        while(ar[j]+k>=ar[x]&&(x<n))
        {
            x++;
        }
        c++;
        i=x;
    }

    return c;
}

int main()
{
    vector<int> arr({7,2,4,6,5,9,12,11});
    cout << "Ans: "<<hackerlandRadioTransmitters(arr,2);
    return 0;
}
