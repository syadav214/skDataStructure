import java.util.Scanner;

class rotate_array {
    public static final Scanner cin = new Scanner(System.in);

    public static void main(String[] args) {
        int T = cin.nextInt();
        while (T != 0) {
            int N = cin.nextInt();
            int D = cin.nextInt();
            int[] arr = new int[N];

            int i = 0;
            while (i <= N - 1) {
                arr[i] = cin.nextInt();
                i++;
            }

            arr = leftRotate(arr, D, N);
            printArray(arr, N);
            System.out.println("");

            T--;
        }
    }

    private static int[] leftRotate(int arr[], int d, int n) {
        int i, j, k, temp;
        int g_c_d = gcd(d, n);
        System.out.print("GCD:");
        System.out.println(g_c_d);

        for (i = 0; i < g_c_d; i++) {
            /* move i-th values of blocks */
            temp = arr[i];
            j = i;
            while (true) {
                k = j + d;
                System.out.print("k:");
                System.out.println(k);
                if (k >= n)
                    k = k - n;
                if (k == i)
                    break;
                arr[j] = arr[k];
                j = k;
                System.out.print("j:");
                System.out.println(j);
            }
            arr[j] = temp;
        }
        return arr;
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }

    private static void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
    }

    private static void rotateArray(int[] arr, int N, int D) {
        String result = "";
        for (int i = D; i < N; i++) {
            result += Integer.toString(arr[i]) + " ";
        }
        for (int i = 0; i < D; i++) {
            result += Integer.toString(arr[i]) + " ";
        }
        System.out.print(result);
    }
}