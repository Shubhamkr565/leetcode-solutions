class SortedArr:
    def search(self, arr):
        n = len(arr)
        target = 40

        for i in range(n):
            if arr[i] == target:
                print(f"Target value {target} is found at index {i}")
                return
        
        print("Target not found")

arr = [10, 20, 30, 40, 50]

print(arr)

s1 = SortedArr()
s1.search(arr)