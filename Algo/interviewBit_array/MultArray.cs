using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

public class Test
{
    public void TestFun()
    {
        List<int> A = new List<int>();
        A.Add(1);
        A.Add(3);
        A.Add(5);
        A.Add(7);
        A.Add(9);
        A.Add(11);
        A.Add(13);
        A.Add(15);
        A.Add(17);
        A.Add(19);

        int sumEven = 0, eventCnt = 0;
        int sumOdd = 0, oddCnt = 0;
        for (int i = 0; i < A.Count; i++)
        {
            if (i % 2 == 0)
            {
                //even
                switch (eventCnt)
                {
                    case 0:
                        sumEven = A[i];
                        break;
                    case 1:
                        sumEven = sumEven * A[i];
                        break;
                    case 2:
                        sumEven += A[i];
                        eventCnt = 0;
                        break;
                }
                eventCnt++;
            }
            else
            {
                //odd
                switch (oddCnt)
                {
                    case 0:
                        sumOdd = A[i];
                        break;
                    case 1:
                        sumOdd = sumOdd * A[i];
                        break;
                    case 2:
                        sumOdd += A[i];
                        oddCnt = 0;
                        break;
                }
                oddCnt++;
            }
        }

        int modEven = sumEven % 2;
        int modOdd = sumOdd % 2;

        if (modOdd > modEven)
        {
            Console.WriteLine("ODD");
        }
        else if (modEven > modOdd)
        {
            Console.WriteLine("EVEN");
        }
        else
        {
            Console.WriteLine("NEUTRAL");    
        }

        Console.WriteLine("Even");
        Console.WriteLine(sumEven.ToString());
        Console.WriteLine("Odd");
        Console.WriteLine(sumOdd.ToString());
    }
}


