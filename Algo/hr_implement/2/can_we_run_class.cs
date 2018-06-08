using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        //convert string array to array of int using linq
        int k =7,on_timers=0;
        int[] a = "26 94 -95 34 67 -97 17 52 1 86".Split(' ').Select(x=> int.Parse(x)).ToArray();

        for(int i=0;i<a.Length;i++)
        {
            if(a[i]<1)
            {
                on_timers++;
            }
        }

        if(on_timers >=k)
        {
            Console.WriteLine("No");
        }
        else
        {
            Console.WriteLine("Yes");
        }
    }
}