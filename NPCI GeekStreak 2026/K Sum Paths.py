'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        # code here
        from collections import defaultdict
        self.count=0
        prefix = defaultdict(int)
        prefix[0] = 1
        def dfs(node,currSum):
            if not node:
                return 
            currSum += node.data
            self.count += prefix[currSum - k]
            prefix[currSum] += 1
            dfs(node.left,currSum)
            dfs(node.right,currSum)
            
            prefix[currSum] -= 1
        dfs(root,0)
        return self.count
        