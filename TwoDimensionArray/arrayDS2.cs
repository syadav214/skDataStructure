//maximum hourglass sum.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class arrayDS2
    {
        public void Main()
        {
            int[][] arr = new int[6][];
            int sum = 0;
            int maxLen = 5;
            for (int arr_i = 0; arr_i < 6; arr_i++)
            {
                string[] arr_temp = Console.ReadLine().Split(' ');
                arr[arr_i] = Array.ConvertAll(arr_temp, Int32.Parse);
            }

            for (int i = 0; i < 6; i++)
            {
                for (int j = 0; j < 6; j++)
                {
                    int tempSum = 0;
                    int nextC2 = j + 1;
                    int nextC3 = j + 2;
                    int nextR2 = i + 1;
                    int nextR3 = i + 2;

                    if (nextC2 <= maxLen && nextC3 <= maxLen && nextR2 <= maxLen && nextR3 <= maxLen)
                    {
                        tempSum = arr[i][j] + arr[i][nextC2] + arr[i][nextC3] + arr[nextR2][nextC2] + arr[nextR3][j] + arr[nextR3][nextC2] + arr[nextR3][nextC3];

                        if (i == 0 && sum == 0)
                        {
                            sum = tempSum;
                        }
                        else if (tempSum > sum)
                        {
                            sum = tempSum;
                        }
                    }
                }
            }
            Console.WriteLine(sum);
        }
    }
}
