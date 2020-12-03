import java.util.LinkedList;
import java.util.Queue;

class Node {
    int value;
    Node left;
    Node right;

    Node(int _value) {
        value = _value;
        left = null;
        right = null;
    }
}

class Tree {
    public Node BuildTree(String[] arr) {
        Node root = new Node(Integer.parseInt(arr[0]));
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        int i = 1;
        while (q.size() > 0 && i < arr.length) {
            Node currNode = q.peek();
            q.remove();

            String currVal = arr[i];
            if (!currVal.equals("N")) {
                currNode.left = new Node(Integer.parseInt(currVal));
                q.add(currNode.left);
            }

            i++;
            if (i >= arr.length)
                break;

            currVal = arr[i];
            if (!currVal.equals("N")) {
                currNode.right = new Node(Integer.parseInt(currVal));
                q.add(currNode.right);
            }
            i++;
        }        
        return root;
    }

    void printInOrder(Node root) {
        if (root == null)
            return;

        printInOrder(root.left);
        System.out.print(root.value + " ");
        printInOrder(root.right);
    }

    Node MergeTreeNodes(Node T1, Node T2) {
        if(T1 == null){
            return T2;
        }

        if(T2 == null){
            return T1;
        }

        T1.value += T2.value;
        T1.left = MergeTreeNodes(T1.left, T2.left);
        T1.right = MergeTreeNodes(T1.right, T2.right);
        return T1;
    }
}


class test {

    public static void main(String[] args) {
        Tree treeNode = new Tree();  

        String[] arr = new String[] { "1", "3", "2", "5", "N"};
        Node T1 = treeNode.BuildTree(arr);
        treeNode.printInOrder(T1);
        
        System.out.println("");

        String[] arr2 = new String[] { "2", "1", "3", "N", "4", "N", "7"};
        Node T2 = treeNode.BuildTree(arr2);
        treeNode.printInOrder(T2);

        System.out.println("");

        Node mergedTree = treeNode.MergeTreeNodes(T1, T2);
        treeNode.printInOrder(mergedTree);
    }
}