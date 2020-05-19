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

class heightOfTree {
    static Node buildTrNode(String str) {
        if (str.length() == 0 || str.charAt(0) == 'N') {
            return null;
        }

        String[] ip = str.split(" ");
        Node root = new Node(Integer.parseInt(ip[0]));

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        int i = 1;
        // 10 20 30 40 60 N N
        while (q.size() > 0 && i < ip.length) {
            Node currNode = q.peek();
            q.remove();

            String currVal = ip[i];
            if (!currVal.equals("N")) {
                currNode.left = new Node(Integer.parseInt(currVal));
                q.add(currNode.left);
            }

            i++;
            if (i >= ip.length)
                break;

            currVal = ip[i];
            if (!currVal.equals("N")) {
                currNode.right = new Node(Integer.parseInt(currVal));
                q.add(currNode.right);
            }
            i++;
        }
        
        return root;
    }

    static void printInOrder(Node root) {
        if (root == null)
            return;

        printInOrder(root.left);
        System.out.print(root.data + " ");
        printInOrder(root.right);
    }

    static void printPreOrder(Node root) {
        if (root == null)
            return;

        System.out.print(root.data + " ");
        printPreOrder(root.left);
        printPreOrder(root.right);
    }

    static void printPostOrder(Node root) {
        if (root == null)
            return;

        printPostOrder(root.left);
        printPostOrder(root.right);
        System.out.print(root.data + " ");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String s = br.readLine(); // s = 10 20 30 40 60 N N
            Node root = buildTrNode(s);
            // printPostOrder(root);
            Tree g = new Tree();
            System.out.println(g.height(root));

        }
    }
}

class Tree {
    // height or depth
    int height(Node node) {
        if (node == null) {
            return 0;
        }

        int lHeight = height(node.left);
        int rHeight = height(node.right);
        if (lHeight > rHeight) {
            return lHeight + 1;
        } else {
            return rHeight + 1;
        }
    }
}
//https://www.youtube.com/watch?v=TQI_m32_AeU