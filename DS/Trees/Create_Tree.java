import java.io.*;
import java.util.*;

class test {
    static class Node {
        int value;
        Node left;
        Node right;
        Node(int value){
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    public void insert(Node n, int v){
        if(v < n.value){
            //left
            if(n.left!=null){
                insert(n.left, v);
            } else {
                n.left = new Node(v);
            }
        } else {
            //right
            if(n.right!=null){
                insert(n.right, v);
            } else {
                n.right = new Node(v);
            }
        }
    }

    public void traverseLevelOrder(Node node){
        if (node != null) {
            traverseLevelOrder(node.left);
            System.out.print(" " + node.value);
            traverseLevelOrder(node.right);
        }
    }

    public static void main(String[] args) {
        test t = new test();
        Node root = new Node(5);
        System.out.println("Binary Tree Example");
        System.out.println("Building tree with root value " + root.value);
        t.insert(root, 2);
        t.insert(root, 4);
        t.insert(root, 8);
        t.insert(root, 6);
        t.insert(root, 7);
        t.insert(root, 3);
        t.insert(root, 9);
        System.out.println("Traversing tree in order");
        t.traverseLevelOrder(root);
    }
}

/// started from 5
/*
        5
       /  \
      2    8
      \   / \
       4  6  9
       /   \
      3     7

*/