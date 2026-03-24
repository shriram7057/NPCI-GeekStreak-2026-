from collections import deque
class Solution:
    def canFinish(self, n, prerequisites):
        # code here 
        adj = [[]for _ in range(n)]
        indegree = [0] * n
        
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        q = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return count == n