"""
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

"""

def PeekIndex(arr):
    start = 0
    end = 0

    while(start <= end):
        mid = start + (end-start)//2

        if(arr[mid-1] < arr[mid] > arr[mid+1]):
            return mid
         
        if(arr[mid-1] > arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return -1


if __name__ == "__main__":
    arr = [4,2,7,3,9,1,8]
    print(f"Index: {PeekIndex(arr)}")