package DSA_Series_in_Java;

class Solution {

    public int findPages(int[] arr, int k) {
        int n = arr.length;

        // ❌ Not possible if students > books
        if (k > n) return -1;

        int low = 0, high = 0;

        // 🔹 Find range
        for (int i = 0; i < n; i++) {
            low = Math.max(low, arr[i]); // max element
            high += arr[i];              // total sum
        }

        int result = -1;

        // 🔹 Binary Search
        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (isPossible(arr, k, mid)) {
                result = mid;
                high = mid - 1; // try smaller value
            } else {
                low = mid + 1;  // increase limit
            }
        }

        return result;
    }

    // 🔹 Greedy check
    private boolean isPossible(int[] arr, int k, int maxPages) {
        int students = 1;
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {

            if (sum + arr[i] > maxPages) {
                students++;
                sum = arr[i];
            } else {
                sum += arr[i];
            }
        }

        return students <= k;
    }
}