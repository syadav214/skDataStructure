import java.util.Scanner;

class test {
    private static Scanner cin = new Scanner(System.in);

    public static void main(String[] args) {
        int n = cin.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = cin.nextInt();
            }
        }
        printInSpiralForm(matrix, n);
    }
    //1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    static void printInSpiralForm(int[][] matrix, int n) {
        int r = 0, c = 0;
        while(true){
            for(int i=c; i < n; i++){
                System.out.print(matrix[r][i]+ " ");
                c++;
            }
            r++;
            c--;

            for(int i=r; i < n; i++){
                System.out.print(matrix[i][c]+ " ");
                r++;
            }

            r--;
            c--;

            for(int i=c; i > -1; i--){
                System.out.print(matrix[r][i]+ " ");
                c--;
            }

            r--;
            c++;
            
            for(int i=r; i > -1; i--){
                System.out.print(matrix[i][c]+ " ");
                r--;
            }
            break;
        }        
    }
}