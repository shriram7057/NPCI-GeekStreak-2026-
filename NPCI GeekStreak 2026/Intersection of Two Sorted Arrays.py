class Solution:
    def intersection(self,a, b):
        # code here
        i,j = 0,0
        n,m = len(a),len(b)
        res = []
        
        while i < n and j < m:
            if a[i] == b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
        