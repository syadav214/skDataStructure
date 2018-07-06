using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int[] p = {2,3,1};

        for(int i=0;i<p.Length;i++)
        {
            int x = i + 1;
            int firstIndex = Array.IndexOf(p,x);
            x = Array.IndexOf(p,firstIndex+1);
            Console.WriteLine(x+1);
        }
    }
}