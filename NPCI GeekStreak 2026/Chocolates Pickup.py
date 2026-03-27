class Solution:
    def maxChocolate(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        dp = [[[-1]* m for _ in range (m)] for _ in range(n)]
        def dfs(i,j1,j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return -10**9
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]
            
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            maxi = -10**9
            
            for dj1 in [-1,0,1]:
                for dj2 in [-1,0,1]:
                    if j1 == j2:
                        val = grid[i][j1]
                    else:
                        val = grid[i][j1] + grid[i][j2]
                    val += dfs(i+1,j1+dj1,j2+dj2)
                    maxi = max(maxi,val)
            dp[i][j1][j2] = maxi
            return maxi
        return dfs(0,0,m-1)
        