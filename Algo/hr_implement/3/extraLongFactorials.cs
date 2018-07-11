using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int n = 5, multi=1;
        int x = n;

        for(int i=0;i<n-1;i++)
        {
            multi = multi * x;
            x = x- 1;
        }

        Console.WriteLine(multi);
    }
}