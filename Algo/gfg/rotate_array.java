import java.util.Scanner; 

class rotate_array {
    public static final Scanner cin=new Scanner(System.in);
	public static void main(String[] args){
		int T=cin.nextInt();
		while(T!=0){
            int N = cin.nextInt();
            int D = cin.nextInt();
            int[] arr= new int[N];

            int i=0;
            while(i <= N-1){
                arr[i] = cin.nextInt();
                i++;
            }

            rotateArray(arr,N,D);
            
			T--;
		}
    }
    
    private static void rotateArray(int[] arr,int N, int D){
        String result= "";
        for(int i=D;i<N;i++){
            result += Integer.toString(arr[i]) + " ";
        } 
        for(int i=0;i<D;i++){
            result += Integer.toString(arr[i]) + " ";            
        }   
        System.out.println("_________________ANSWER__________________");    
        System.out.println(result);
    }
}