class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)
        
        res = []
        
        while i < n1 and j < n2 and k < n3:
            if a[i] == b[j] == c[k]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                mn = min(a[i], b[j], c[k])
                if a[i] == mn:
                    i += 1
                if b[j] == mn:
                    j += 1
                if c[k] == mn:
                    k += 1
        
        return res