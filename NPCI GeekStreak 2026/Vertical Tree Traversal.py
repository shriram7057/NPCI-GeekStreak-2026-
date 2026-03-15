'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        if not root:
            return []
        
        from collections import defaultdict,deque
        column_map=defaultdict(list)
        q=deque()
        q.append((root,0))
        
        min_hd=0
        max_hd=0
        
        while q:
            node , hd=q.popleft()
            
            column_map[hd].append(node.data)
            
            min_hd= min(min_hd,hd)
            max_hd= max(max_hd,hd)
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
        # return []
        result =[]
        for hd in range(min_hd,max_hd+1):
            result.append(column_map[hd])
        return result