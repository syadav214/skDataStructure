import java.util.HashMap;
import java.util.Scanner;
import java.util.LinkedList; 
import java.util.Queue; 

class Ops {
    HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();

    void insert(Queue<Integer> q, int k) {
        q.add(k);
        if (hashMap.containsKey(k)) {
            hashMap.put(k, hashMap.get(k) + 1);
        } else {
            hashMap.put(k, 1);
        }
    }

    int findFrequency(Queue<Integer> q, int k) {
        Integer[] qArr = q.toArray(new Integer[q.size()]);
        int count = 0;
        for(int i=0;i<q.size();i++){
            if(qArr[i] == k) {
                count++;
            }
        }
        return count;

 
        /*if (hashMap.containsKey(k)) {
            return hashMap.get(k);
        } else {
            return 0;
        }*/
    }
}

public class queueOperations {
    private static Scanner cin = new Scanner(System.in);

    public static void main(String[] args) {
        int t = cin.nextInt();
        while (t-- > 0) {
            int m = cin.nextInt();
            Ops ops = new Ops();
            int i = 0;
            Queue<Integer> queue = new LinkedList<>();
            while (i < m) {
                int num = cin.nextInt();
                ops.insert(queue, num);
                i++;
            }

            int n = cin.nextInt();
            i = 0;
            while (i < n) {
                int num = cin.nextInt();
                int f = ops.findFrequency(queue, num);
                if (f != 0) {
                    System.out.println(f);
                } else {
                    System.out.println(-1);
                }
                i++;
            }
        }
    }
}