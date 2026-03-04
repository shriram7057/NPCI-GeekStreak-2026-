class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n = len(arr)
        curr_xor = 0
        for i in range(k):
            curr_xor ^= arr[i]
        max_xor = curr_xor
        
        for i in range(k,n):
            curr_xor ^= arr[i-k]
            curr_xor ^= arr[i]
            if curr_xor > max_xor:
                max_xor = curr_xor
        return max_xor
       