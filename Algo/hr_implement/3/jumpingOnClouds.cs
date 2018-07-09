using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int[] c = {0, 0, 1, 0, 0, 1, 1, 0};
	    int E =100,k = 2;

        for(int i=0;i<c.Length;i=i+k)
        {
            int subVal = 1;
            if(c[i]==1)
            {
                subVal +=2;
            }
            E = E - subVal;
        }

        Console.WriteLine(E);
    }
}