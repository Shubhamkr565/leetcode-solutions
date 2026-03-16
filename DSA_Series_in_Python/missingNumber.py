"""You are given an array containing numbers from 0 to n, but one number is missing.

Your job is to find the missing number."""

def missingNumber(nums):
    n = len(nums)
    result = n

    for i in range(n):
        result ^= i
        result ^= nums[i]
    return result

if __name__ == "__main__":
    arr = [0,4,1,3]
    print(missingNumber(arr))