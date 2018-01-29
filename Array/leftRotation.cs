using System;
using System.Linq;

namespace ConsoleApplication1
{
    class leftRotation
    {
        public void Main()
        {
            int d = int.Parse(Console.ReadLine());
            string raw = Console.ReadLine();
            string[] a = raw.Split(' ');
            string[] finalArray = new string[a.Length];
            for(int i=0;i< a.Length; i++)
            {
                var index = i -d;
                if(index < 0)
                {
                    index = a.Length + index;
                }
                finalArray[index] = a[i];
            }
            Console.WriteLine(string.Join(" ", finalArray.Select(x=> x.ToString())));
        }

    }
}
