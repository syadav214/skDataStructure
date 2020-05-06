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

class test {
    static Node buildTrNode(String str) {
        if (str.length() == 0 || str.charAt(0) == 'N') {
            return null;
        }

        String[] ip = str.split(" ");
        Node root = new Node(Integer.parseInt(ip[0]));

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        int i = 1;
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

    static void printInorder(Node root) {
        if (root == null)
            return;

        printInorder(root.left);
        System.out.print(root.data + " ");
        printInorder(root.right);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String s = br.readLine();
            Node root = buildTrNode(s);
            //printInorder(root);
            Tree g = new Tree();
            System.out.println(g.height(root));

        }
    }
}

class Tree {
    int height(Node node) {
        return 1;
    }
}