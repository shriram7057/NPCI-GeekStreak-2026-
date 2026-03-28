class Solution:
    def articulationPoints(self, V, edges):
        # code here
        from collections import defaultdict
        adj=defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        timer = 0
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        ap=[False] * V
        
        def dfs(u):
            nonlocal timer
            disc[u] = low[u] =timer
            timer += 1
            children= 0
            
            for v in adj[u]:
                if disc[v] == -1:
                    parent[v]=u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u],low[v])
                    
                    if parent[u] == -1 and children > 1:
                        ap[u] =True
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u]=True
                elif v != parent[u]:
                    low[u]= min(low[u],disc[v])
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
        res= [i for i in range(V) if ap[i]]
        return res if  res else [-1]
                