//Sparse Arrays
using System;

namespace ConsoleApplication1
{
    class SparseArray
    {
        public void Main()
        {
            int N = int.Parse(Console.ReadLine());
            string[] Nstring = new string[N];
            for(int i=0;i< N;i++)
            {
                Nstring[i] = Console.ReadLine();
            }

            int Q = int.Parse(Console.ReadLine());
            for (int i = 0; i < Q; i++)
            {
                string Qsearch = Console.ReadLine();
                int count = 0;
                for (int j = 0; j < N; j++)
                {
                    if(Qsearch == Nstring[i])
                    {
                        count++;
                    }
                }
                Console.WriteLine(count);
            }
            

        }

    }
}
