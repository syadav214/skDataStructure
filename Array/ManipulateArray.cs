/*
Difference array will as below:
Rather than adding element to in ranges between a and b.
We will add in a - 1 and subtract from b.
Then in for loop for all the elements of nArray, we will add every variable;
it will add +ve and -ve values;
 */

using System;

namespace ConsoleApplication1
{
    class ManipulationArray
    {
        public void Main()
        {
            string[] nm = Console.ReadLine().Split(' ');
            
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            int[] nArray = new int[n+1];

            for(int i=0;i< m;i++)
            {
                string[] abk = Console.ReadLine().Split(' ');
                int a = int.Parse(abk[0]);
                int b = int.Parse(abk[1]);
                int k = int.Parse(abk[2]);
                nArray[a-1] += k;
                if (b <= nArray.Length)
                    nArray[b] -= k;
            }

            int max = 0, temp = 0;

            foreach(var i in nArray)
            {
                temp = temp + i;
                if (temp > max)
                    max = temp;
            }

            Console.WriteLine(max);
        }
    }
}
