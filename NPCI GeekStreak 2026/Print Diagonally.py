class Solution:
    def diagView(self, mat): 
        # code here
        n = len(mat)
        res =[]
        for d in range(n):
            i,j = 0,d
            while j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
        for d in range(1,n):
            i,j = d,n - 1
            while i <n:
                res.append(mat[i][j])
                i += 1
                j -= 1
        return res