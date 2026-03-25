from collections import deque
class Solution:
    def minHeightRoot(self, V, edges):
        # Code here
        if V == 1:
            return [0]
        adj = [[]for _ in range(V)]
        degree =[0] * V
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        q = deque()
        
        for i in range(V):
            if degree[i] == 1:
                q.append(i)
        remaining = V
        
        while remaining > 2:
            size = len(q)
            remaining -= size
            
            for _ in range(size):
                node = q.popleft()
                
                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        return list(q)
