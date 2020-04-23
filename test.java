import java.util.Scanner; 

class test {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i = 0;i < T;i++) {   
            System.out.print("i");     
            System.out.print(i);     
            String[] arrSizeRotation = sc.nextLine().split(" ");
            for(String v: arrSizeRotation){
                System.out.print(v);
            }
        }
	}
}