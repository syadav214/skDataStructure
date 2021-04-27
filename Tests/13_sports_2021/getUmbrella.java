/*
Monsoon Umbrellas Umbrellas are available in different sizes that are each able to shelter a certain number of people. 
Given the number of people needing shelter and a list of umbrella sizes, determine the minimum number of umbrellas necessary to
 cover exactly the number of people given, and no more.
  If there is no combination that covers exactly that number of people, return -1. 
  Example requirement=5 sizes = 13,5 One umbrella can cover exactly 5 people, so the function should return 1. 
  Example requirement = 6 sizes = [3,5,7]
 It is possible to use 2 umbrellas of size 3 to cover exactly 6 people, so the function should return 2.

*/

import java.io.*;
import java.util.*;

class test {
    

    public static void main(String[] args) {        
        List<Integer> sizes = new ArrayList<>();
        //sizes.add(2);
        sizes.add(3);
        //sizes.add(4);
        //sizes.add(5);
        //sizes.add(7);
        System.out.println(umbrella(sizes));
    }

    static int umbrella(List<Integer> sizes){
        int requirement = 5;
        for(int i =0;i<sizes.size();i++){
            int currElemt = sizes.get(i);
            System.out.print("currElemt:");
            System.out.println(currElemt);
            if(currElemt > requirement){
                continue;
            } else {
                int q = requirement /currElemt;
                System.out.print("Q:");
                System.out.println(q);
                int r = requirement % currElemt;
                System.out.print("R:");
                System.out.println(r);
                if(r == 0){
                    return q;
                }
                for(int j =0;j<sizes.size();j++){
                    int curr2 = sizes.get(j);
                    System.out.print("curr2:");
                    System.out.println(curr2);
                    if(curr2 == r){
                        System.out.print("value:");
                        System.out.println(q+1);
                        return q +1;
                    }
                }
            }
        }
        return -1;
    }
}

