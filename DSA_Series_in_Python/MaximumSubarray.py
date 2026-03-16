"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6."""

def maxSubArr(nums):
    n = len(nums)
    curSum = 0
    maxSum = nums[0]

    for i in range(n):
        curSum += nums[i]
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArr(arr))