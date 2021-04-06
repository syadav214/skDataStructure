import java.util.LinkedList;
import java.util.Queue;

class test {

    public static void main(String[] args) {
        int[][] matrix = { {0 ,1 ,1, 1}, {0 ,0, 1, 1},  {1, 1, 1, 1}, {0, 0 ,0 ,0 } };
        int max_row_index = -1, max_count = 0;
        for(int r=0;r< matrix.length;r++){
            for(int c=0;c< matrix.length;c++){
                if(matrix[r][c] == 1){
                    int count = matrix.length - c;
                    if(count > max_count){
                        max_count = count;
                        max_row_index = r;
                    }                    
                    break;
                }
            }
        }
        System.out.println(max_row_index);
    }
}