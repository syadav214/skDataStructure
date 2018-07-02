using System;
using System.Linq;
using System.Collections;

public class Test
{
    public void TestFun()
    {
       int n =3,likes=0,refer=3;;
       double ads=5;

       for(int i=1;i<=n;i++)
       {
           int tmp_like = (int) Math.Floor(ads/2);
           likes += tmp_like;
           ads = tmp_like * refer;
       }

       Console.WriteLine(likes);
    }
}