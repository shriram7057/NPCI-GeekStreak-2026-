class Solution {
    public int minTime(int[] arr, int k) {
        int n = arr.length;

        int low = 0;
        int high = 0;

        // Find max element and total sum
        for (int i = 0; i < n; i++) {
            low = Math.max(low, arr[i]);
            high += arr[i];
        }

        int ans = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canPaint(arr, k, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }

    private boolean canPaint(int[] arr, int k, int maxTime) {
        int painters = 1;
        int currSum = 0;

        for (int length : arr) {
            if (currSum + length <= maxTime) {
                currSum += length;
            } else {
                painters++;
                currSum = length;

                if (painters > k) {
                    return false;
                }
            }
        }

        return true;
    }
}