using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int nOfPrisoners=4, candies=6, startingPoint=2,warn=0;

        warn = ((startingPoint-1) + candies) % nOfPrisoners;

        if(warn == 0)
        {
            Console.WriteLine(nOfPrisoners);
        }
        else
        {
            Console.WriteLine(warn);
        }
    }
}