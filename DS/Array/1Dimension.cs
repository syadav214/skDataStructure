//reverse order of array
using System;

namespace ConsoleApplication1
{
    class arrayDS1
    {
        public void Main()
        {
            string arrayCount = Console.ReadLine();
            string arrayData = Console.ReadLine();
            string[] intData = arrayData.Split(' ');
            string printdata = "";

            for(int i=intData.Length - 1;i>=0;i--)
            {
                printdata = printdata + intData[i] + ' ';
            }
            Console.WriteLine(printdata);

        }
        
    }
}
