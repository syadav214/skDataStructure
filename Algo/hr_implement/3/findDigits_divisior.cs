using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int n = 1012, count = 0;
        foreach (var x in Convert.ToString(n))
        {
            if (x != '0' && n % Convert.ToInt16(Convert.ToString(x)) == 0)
            {
                count++;
            }
        }
        Console.WriteLine(count);
    }
}