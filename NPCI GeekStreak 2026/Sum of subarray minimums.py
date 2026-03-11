class Solution:
    def sumSubMins(self, arr):
        # code here
        n = len(arr)
        
        left = [0]* n
        right = [0]* n
        
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i]= i - stack[-1]
            stack.append(i)
        stack.clear()
        
        for i in range(n-1, -1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                right[i] = stack[-1] - i
            stack.appned(i)
            
        res = 0
        
        for i in range(n):
            res += arr[i] * left[i] * right[i]
        return res