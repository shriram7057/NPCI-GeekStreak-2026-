class Solution:
    def countSubarrays(self, arr):
        # code here
        n = len(arr)
        stack = []
        res = 0
        
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                res += n - i
            else:
                res += stack[-1] - i
            stack.append(i)
        return res