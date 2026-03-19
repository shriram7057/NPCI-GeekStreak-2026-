class Solution:
    def largestBst(self, root):
        # Your code here
        self.max_size = 0
        def dfs(node):
            if not node:
                return (True,0,float('inf'),float('-inf'))
            left  = dfs(node.left)
            right = dfs(node.right)
            
            if left[0] and right[0] and left[3] < node.data < right[2]:
                size = left[1] + right[1] + 1
                self.max_size = max(self.max_size,size)
                return (True,size,min(left[2],node.data),max(right[3],node.data))
            else:
                return(False,0,0,0)
        dfs(root)
        return self.max_size