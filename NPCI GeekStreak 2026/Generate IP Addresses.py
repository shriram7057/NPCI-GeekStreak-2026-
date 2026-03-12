#Your Function should return a list containing all possible IP address

class Solution:
    def generateIp(self, s):
        # Code here
        n=len(s)
        res=[]
        def valid(seg):
            if len(seg)>1 and seg[0]=='0':
                return False
            return 0 <= int(seg)<=255
        for i in range(1,4):
            A=s[:i]
            if not valid(A):
                continue
            for j in range(i+1,min(i+4,n)):
                B=s[i:j]
                if not valid(B):
                    continue
                for k in range(j+1,min(j+4,n)):
                    C=s[j:k]
                    D=s[k:]
                    if valid(C) and valid(D):
                        res.append(A + "." + B + "." + C + "." + D)
        return res