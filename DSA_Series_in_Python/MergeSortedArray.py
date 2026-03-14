"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    
    Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    """

class Solution:
    def MergeSorted(self, num1, num2):
        i = 0
        j = 0
        num3 = []

        while i<len(num1) and j<len(num2):
            if num1[i] <= num2[j]:
                num3.append(num1[i])
                i +=1
            else:
                num3.append(num2[j])
                j += 1
        
        while i<len(num1):
            num3.append(num1[i])
            i +=1
        
        while j<len(num2):
            num3.append(num2[j])
            j += 1
        return num3
    
if __name__ == "__main__":
    num1 = [1,2,3]
    num2 = [2,5,6]

    obj = Solution()
    print(num1)
    print(num2)
    print(obj.MergeSorted(num1, num2))