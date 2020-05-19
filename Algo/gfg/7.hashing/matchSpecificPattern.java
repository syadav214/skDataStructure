import java.util.*;

/* INPUT: abb abc xyz xyy
          foo
   OUTPUT: abb xyy
*/
class matchSpecificPattern {
    public static void main(String[] main) {
        Scanner cin = new Scanner(System.in);
        int t = cin.nextInt();
        while (t-- > 0) {
            int n = cin.nextInt();
            ArrayList<String> s = new ArrayList<String>(n);
            for (int i = 0; i < n; i++) {
                s.add(cin.next());
            }

            String tt = cin.next();
            Hash h = new Hash();
            ArrayList<String> res = h.findMatchedWords(s, tt);
            Collections.sort(res);
            
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + " ");
            }
        }
    }
}

class Hash {
    public ArrayList<String> findMatchedWords(ArrayList<String> dict, String pattern) {
        ArrayList<String> arr = new ArrayList<>();
        String patternEncode = encode(pattern);
        int len = pattern.length();

        for(String str: dict){
            if(str.length() == len && encode(str).equals(patternEncode)){
                arr.add(str);
            }
        }
        return arr;        
    }

    private String encode(String str){
        HashMap<Character, Integer> hMap = new HashMap<>();
        int i = 0;
        Character ch;
        String res = "";
        for(int j=0; j < str.length();j++){
            ch = str.charAt(j);
            // assigning a unique number to character; it will assign only one time
            if(!hMap.containsKey(ch)){
                hMap.put(ch, i++);
            }

            // so if we have str 'abb', so the res can be '122'
            res += hMap.get(ch);
        }
        System.out.print(res+" ");
        return res;
    }
}