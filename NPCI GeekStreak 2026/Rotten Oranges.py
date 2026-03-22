from collections import deque
class Solution:
    def orangesRot(self, mat):
        # code here
        rows,cols=len(mat),len(mat[0])
        q=deque()
        fresh=0
        for i in range(rows):
            for c in range(cols):
                if mat[i][c]==2:
                    q.append((i,c,0))
                elif mat[i][c]==1:
                    fresh +=1
        time=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,t=q.popleft()
            time=max(time,t)
            
            for dr,dc in directions:
                nr , nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc < cols and mat[nr][nc]==1:
                    mat[nr][nc]=2
                    fresh -= 1
                    q.append((nr,nc,t+1))
        return time if fresh ==0 else -1