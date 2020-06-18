import java.util.*;

public class firstNonRepeatingNumber {
    public static void main(String[] args) {
        int[] arr = new int[] {2,2,2,3,3,1,2,3,5,4,3,9,0,2};
        HashMap<Integer, Integer> hMap = new HashMap<>();

        for(int i: arr){
            if(hMap.containsKey(i)){
                hMap.put(i, hMap.get(i) + 1);
            } else {
                hMap.put(i, 1);
            }
        }

        for(int i: arr){
            if(hMap.get(i) == 1){
                System.out.print("Answer: "+ i);
                break;
            }
        }
        
    }
}