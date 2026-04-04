class Solution:
    def graycode(self,n):
        #code here
        res = ["0","1"]
        if n == 1:
            return res
        for i in range(2,n+1):
            rev = res[::-1]
            
            res = ["0" + x for x in res]
            
            res += ["1" + x for x in rev]
        return res