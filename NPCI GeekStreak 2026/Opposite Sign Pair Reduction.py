class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for x in arr:
            while stack and stack[-1] * x < 0:
                top = stack[-1]
                
                if abs(top) > abs(x):
                    x = top
                    stack.pop()
                elif abs(top) < abs(x):
                    stack.pop()
                else:
                    stack.pop()
                    x = 0
                    break
            
            if x != 0:
                stack.append(x)
        
        return stack