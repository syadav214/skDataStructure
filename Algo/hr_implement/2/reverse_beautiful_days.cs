using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
       int i=20,j=23,k=6,count=0;

       for(int x = i;x<=j;x++)
       {
           char[] reverse_char = Convert.ToString(x).ToCharArray();
           Array.Reverse(reverse_char);
           int reverse_num = Convert.ToInt32(new String(reverse_char));
           
           if((Math.Abs(x-reverse_num))%k==0)
           {
               count++;
           }
       }
       Console.WriteLine(count);
    }
}