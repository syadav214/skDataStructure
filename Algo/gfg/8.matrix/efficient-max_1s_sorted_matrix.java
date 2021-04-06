import java.util.LinkedList;
import java.util.Queue;

class test {

    public static void main(String[] args) {
        int[][] matrix = { {0 ,1 ,1, 1}, {0 ,0, 1, 1},  {1, 1, 1, 1}, {0, 0 ,0 ,0 } };
        int c= 4;
        
        int j = firstRowIndex(matrix[0], 0, c-1);
        int max_row_index = j;
        if(j == -1){
            j = c - 1;
        }

        for(int i=1;i<c;i++){
            while (j >= 0 && matrix[i][j] == 1){
                j = j - 1;  // Update the index of leftmost 1 seen so far
                max_row_index = i;  // Update max_row_index
            }
        }
        System.out.println(max_row_index);
    }

    static int firstRowIndex(int[] arr, int start, int end) {
        while(start <= end){
            int mid = start + ( end - start) /2;

            if ((mid == 0 || (arr[mid - 1] == 0)) && arr[mid] == 1)
                return mid;
            else if(arr[mid] == 0){
                return firstRowIndex(arr, mid + 1, end);
            } else {
                return firstRowIndex(arr, start, mid - 1);
            }
        }
        return -1;
    }
}