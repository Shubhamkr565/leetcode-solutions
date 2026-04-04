"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

"""


"""class SortedArr:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        for i in range(n):
            if target == nums[i]:
                print(f"Target value {target} is found at index {i}")
                return
            print("Target not found")


nums = [4,5,6,7,0,1,2]
target = 4
s1 = SortedArr()

s1.search(nums, target)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left+ (right-left)//2
            # step1 find the target
            if nums[mid] == target:
                return mid
            # step2 left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid-1  # search left
                else:
                    left = mid+1  # search right
            
            # step3 Right half is Sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    right = mid-1 # search right
                else:
                    left = mid+1 #serach left
        return -1


nums = [10,20,40,50,60]
target = 50
s1 = Solution()

print(f"Index: {s1.search(nums, target)}")
