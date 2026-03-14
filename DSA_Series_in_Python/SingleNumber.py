"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4"""




def SingleNumber(nums):
    result = 0

    for num in nums:
        result ^= num
    return result 

if __name__ == "__main__":
    num = [4,1,2,1,2]
    print(SingleNumber(num))


"""
nums = [4,1,2,1,2]
result = 0
result = 0 ^ 4
result = 4
result = 4 ^ 1
result = 4 ^ 1
result = 4 ^ 1 ^ 2
result = 4 ^ 1 ^ 2 ^ 1 
1 ^ 1 = 0
4 ^ 2
4 ^ 2 ^ 2
2 ^ 2 = 0
4

Same numbers cancel each other
Only the single number remains

"""