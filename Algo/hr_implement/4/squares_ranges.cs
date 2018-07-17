using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int a = 3, b=9;

        double ranges = ((Math.Floor(Math.Sqrt(b))) - (Math.Ceiling(Math.Sqrt(a))) ) + 1;

        Console.WriteLine(ranges.ToString());       

    }
}