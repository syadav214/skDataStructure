using System;
using System.Linq;

public class Test
{
    public void TestFun()
    {
        int[] a = {1, 2, 2, 3, 1, 2};
        int max_count=0;

        foreach(var element in a)
        {
            int count_curr =  a.Where(x=> x==element).Count();
            int count_curr_minus_one = a.Where(x=> x==element-1).Count();
            int sum_of_count = count_curr + count_curr_minus_one;

            if(sum_of_count > max_count)
            {
                max_count = sum_of_count;
            }
        }
        Console.WriteLine(max_count);
    }
}