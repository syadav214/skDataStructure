import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Tree {
    static Node buildTree(String s) {
        if (s.length() == 0 || s.charAt(0) == 'N') {
            return null;
        }

        String[] tV = s.split(" ");
        Node root = new Node(Integer.parseInt(tV[0]));
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        int i = 1;

        while (q.size() > 0 && i < tV.length) {
            Node currNode = q.peek();
            q.remove();

            if (!tV[i].equals("N")) {
                currNode.left = new Node(Integer.parseInt(tV[i]));
                q.add(currNode.left);
            }

            i++;
            if (i >= tV.length)
                break;

            if (!tV[i].equals("N")) {
                currNode.right = new Node(Integer.parseInt(tV[i]));
                q.add(currNode.right);
            }
            i++;
        }
        return root;
    }

    static int minValue(Node node) {
        Node currNode = node;
        // in BST, all small values are on left node, so we are traversing till last
        // left node
        while (currNode.left != null) {
            currNode = currNode.left;
        }
        return currNode.data;
    }
}

class minValueOfBST {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String s = br.readLine(); // s = 5 4 6 3 N N 7 1
            Node root = Tree.buildTree(s);
            int minValue = Tree.minValue(root);
            System.out.println(minValue);
        }
    }
}