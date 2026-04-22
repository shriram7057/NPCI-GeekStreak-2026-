class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        
        # Prefix sum
        prefix = [0]*n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]
        
        res = []
        
        for l, r in queries:
            total = prefix[r] - (prefix[l-1] if l > 0 else 0)
            length = r - l + 1
            res.append(total // length)
        
        return res