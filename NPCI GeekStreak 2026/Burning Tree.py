'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def minTime(self, root, target):
        # code here
        parent = {}
        target_node = [None]
        
        def dfs(node,par):
            # nonlocal target_node
            if not node:
                return
            
            parent[node] = par
            
            if node.data == target:
                target_node[0] = node
                
            dfs(node.left,node)
            dfs(node.right,node)
            
        dfs(root,None)
        
        q = deque([target_node[0]])
        visited = set([target_node[0]])
        time = -1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left , node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            time += 1
            
        return time 