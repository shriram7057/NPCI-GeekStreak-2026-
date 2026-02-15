#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        n = len(arr)
        if M == 0 or n == 0 or M > n:
            return 0 
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff