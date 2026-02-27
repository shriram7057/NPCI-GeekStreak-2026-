class Solution:
    def countSquare(self, mat, x):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        prefix = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                prefix[i][j] =(
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )
        count = 0
        for size in range(1,min(n,m) + 1):
            for i in range(size,n+1):
                for j in range(size,m+1):
                    total = (
                        prefix[i][j]
                        - prefix[i-size][j]
                        - prefix[i][j-size]
                        + prefix[i - size][j - size]
                    )
                    if total == x:
                        count += 1
        return count