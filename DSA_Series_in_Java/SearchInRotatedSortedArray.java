// There is an integer array nums sorted in ascending order (with distinct values).

// Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

// You must write an algorithm with O(log n) runtime complexity.


package DSA_Series_in_Java;

public class SearchInRotatedSortedArray {

    public static int search(int[] arr, int target){
        int left = 0;
        int right = arr.length-1;   

        // step1 find mid
        while(left <= right){
            int mid = left + (right-left)/2;

            // Check mid == target
            if (arr[mid] == target){
                return mid;
            }
            // step2  left half is sorted
            if(arr[left] <=  arr[mid]){
                if(arr[left] <= target && target <= arr[mid]){
                    right = mid-1;
                }else{
                    left = mid+1;
                }
            }else{  // step3 search is right part
                if(arr[mid] <= target && target <= arr[right]){
                    left = mid+1;
                }else{
                    right = mid-1;
                }
            }
        }
        return -1;
    }



    public static void main(String[] args){
        int[] arr = {4,5,6,7,0,1,2};
        int target = 0;

        int result = search(arr, target);
        System.out.println("Index: "+result);
    }
    
}
