package DSA_Series_in_Java;

public class SingleElementInASortedArray {
    public static void  main(String[] args){

        int[] arr = {1,1,2,2,3,4,4,5,5,6,6};

        int start = 0;
        int end = arr.length-1;

        while(start < end){
            int mid = start + (end - start)/2;

            if (mid % 2 == 1){
                mid -= 1;
            }
            if(arr[mid] == arr[mid+1]){
                start = mid+2;
            }else{
                end = mid;
            }
        }
        System.out.println("Single Element: " + arr[start]);

    }
}
