
public class towerOfHanoi {
    public static void main(String[] args) {
        int n = 4; // Number of disks
        // A is where it is placed currently, C is where it to be place
        towerOfHanoi(n, 'A', 'C', 'B');
    }

    static void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod) {
        if (n == 1) {
            System.out.println("move disk 1 from rod " + from_rod + " to rod " + to_rod);
            return;
        }

        // we are diving our problem in smaller one. so we are taking first 3 and leaving 1 out. that why n-1
        towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
        System.out.println("move disk " + n + " from rod " + from_rod + " to rod " + to_rod);
        towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
    }
}