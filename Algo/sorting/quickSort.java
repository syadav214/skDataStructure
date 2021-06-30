

class quickSort {

    public static void main(String[] arg){
        int[] arr = { 5,2,9,4,3,13,90,1,6 };
        int[] finalArr = quickSort(arr);
    }

    static int[] quickSort(int[] arr){
        if(arr.length < 2){
            return arr;
        } else {
            int mid = arr.length/2;
            int pivot = arr[mid];

            int leftSize = 0, rightSize = 0;
            for(int i = 0;i< arr.length;i++){
                if(arr[i] < pivot){
                    leftSize++;
                } else if(arr[i] > pivot){
                    rightSize++;
                }
            }

            int[] leftArr = new int[leftSize];
            int[] rightArr = new int[rightSize];
            int leftI = 0, rightI = 0;
            for(int i = 0;i< arr.length;i++){
                if(arr[i] < pivot){
                    leftArr[leftI] = arr[i];
                    leftI++;
                } else if(arr[i] > pivot){
                    rightArr[rightI] = arr[i];
                    rightI++;
                }
            }

            int[] leftSort = quickSort(leftArr);
            int[] rightSort = quickSort(rightArr);

            int[] finalArr = new int[leftSort.length + rightSort.length + 1];
            int finalI= 0;
            for(int i =0 ;i < leftSort.length;i++){
                finalArr[finalI] = leftSort[i];
                finalI ++;
            }

            finalArr[finalI] = pivot;
            finalI ++;

            for(int i =0 ;i < rightSort.length;i++){
                finalArr[finalI] = rightSort[i];
                finalI ++;
            }


            return  finalArr;
        }
    }
}