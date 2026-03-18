'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        # code here
        self.moves=0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.moves += abs(left) + abs(right)
            return node.data - 1 + left + right
        dfs(root)
        return self.moves