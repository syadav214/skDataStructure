import java.util.Scanner;

class Node {
    int data;
    Node right, down;

    Node(int data) {
        this.data = data;
        right = null;
        down = null;
    }
}

public class matrix {
    private static Scanner cin = new Scanner(System.in);

    public static void main(String[] args) {
        int t = cin.nextInt();
        while (t > 0) {
            int r = cin.nextInt();
            int[][] arr = new int[r][r];
            int i = 0;

            while (i <= r - 1) {
                int c = 0;
                while (c <= r - 1) {
                    arr[i][c] = cin.nextInt();
                    c++;
                }
                i++;
            }

            // arr is ready

            t--;
        }
    }

    public static Node construct(int arr[][], int n) {
        Node node = build(arr, 0, 0, n);
        return node;
    }

    private static Node build(int arr[][], int i, int k, int n) {
        if (i > n - 1 || k > n - 1) {
            return null;
        }

        Node node = new Node(arr[i][k]);
        node.right = build(arr, i + 1, k, n);
        node.down = build(arr, i, k + 1, n);
        return node;
    }
}