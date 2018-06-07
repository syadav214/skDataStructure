using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
        //convert string array to array of int using linq
        int[] h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".Split(' ').Select(str=> int.Parse(str)).ToArray();
	    string word = "zaba";
        int width = word.Length;
        int[] word_height = new int[width];

        for(int i=0;i< width;i++)
        {
            word_height[i] = h[(byte)Convert.ToChar(word[i])-97];
        }

        int height = word_height.Max();
        Console.WriteLine(height*width);
    }
}