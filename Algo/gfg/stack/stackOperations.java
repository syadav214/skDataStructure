import java.util.Scanner;
import java.util.Stack;

class Ops {
    public void insert(Stack<Integer> st, int x) {
        st.add(x);
    }

    public int remove(Stack<Integer> st) {
        int x = st.peek();
        st.pop();
        return x;
    }

    public void headOf_Stack(Stack<Integer> st) {
        int x = st.peek();
        System.out.println(x + " ");
    }

    public void find(Stack<Integer> st, int val) {
        if (st.contains(val)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}

public class stackOperations {
    private static final Scanner cin = new Scanner(System.in);

    public static void main(String[] args) {
        int t = cin.nextInt();
        while (t-- > 0) {
            Stack<Integer> st = new Stack<Integer>();
            int q = cin.nextInt();
            while (q-- > 0) {
                char ch = cin.next().charAt(0);
                Ops obj = new Ops();
                if (ch == 'i') {
                    int i = cin.nextInt();
                    obj.insert(st, i);
                }
                if (ch == 'r') {
                    obj.remove(st);
                }
                if (ch == 'h') {
                    obj.headOf_Stack(st);
                }
                if (ch == 'f') {
                    int i = cin.nextInt();
                    obj.find(st, i);
                }
            }
        }

    }
}