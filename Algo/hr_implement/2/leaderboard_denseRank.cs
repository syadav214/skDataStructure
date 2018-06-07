using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        int[] scores = {100, 100, 50, 40, 40, 20, 10};
        int[] alice = {5, 25, 50, 120};
        int[] result = new int[4];

        //remove duplicate and convert to array
        var y = scores.Distinct().ToArray();
        //sort ascending
        Array.Sort(y);

        int rank=0, leng = y.Length+1,i=0,mid =0;
        double high =0,low=0;

        foreach(var element in alice) 
        {
            rank = leng;
            high = leng -1;

            while(low < high)
            {
                mid = (int) Math.Round((low+high)/2);
                if(y[mid]<=element) 
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid;
                }
            }

            rank -=(int)low;
            result[i] = rank;
            i++;
        }

        foreach(var element in result)
        {
            Console.WriteLine(element);
        }
    }
}