class Solution:
    def findClosestPair(self,arr1, arr2, x):
        #code here
        n = len(arr1)
        m = len(arr2)
        
        i = 0
        j = m - 1
        
        min_diff = float('inf')
        res = [0,0]
        
        while i < n and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)
            
            if diff < min_diff:
                min_diff = diff
                res = [arr1[i],arr2[j]]
            if curr_sum > x:
                j -= 1
            else:
                i += 1
        return res