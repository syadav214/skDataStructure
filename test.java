import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Heap {
    static Node buildHeap(String s){
        if(s.length() == 0 || s.charAt(0) == 'N'){
            return null;
        }

        String[] arr = s.split(" ");
        int currVal = Integer.parseInt(arr[0]);
        Node root = new Node(currVal);

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;

        while(q.size() > 0 && i < arr.length) {
            Node currNode = q.peek();
            q.remove();

            if(!arr[i].equals("N")) {
                currVal = Integer.parseInt(arr[i]);
                currNode.left = new Node(currVal);
                q.add(currNode.left);
            }

            i++;
            if(i >= arr.length){
                break;
            }

            if(!arr[i].equals("N")) {
                currVal = Integer.parseInt(arr[i]);
                currNode.right = new Node(currVal);
                q.add(currNode.right);
            }
            i++;
        }
        return root;
    }

    static void printPreOrder(Node root) {
        if (root == null)
            return;

        System.out.print(root.data + " ");
        printPreOrder(root.left);
        printPreOrder(root.right);
    }

    static int heightOfHeap(Node root) {
        if(root == null){
            return 0;
        }
        int leftHeight = heightOfHeap(root.left);
        int rightHeight = heightOfHeap(root.right);
        if(leftHeight > rightHeight){
            return leftHeight + 1;
        } else {
            return rightHeight + 1;
        }
    }
}

class test {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            String s = br.readLine();
            Node root = Heap.buildHeap(s);            
            //Heap.printPreOrder(root);
            System.out.println(Heap.heightOfHeap(root));
        }
    }
}