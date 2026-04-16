class Solution:
    def myAtoi(self, s):
        # Code here
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i=0 
        if s[0]=='-':
            sign =-1
            i +=1
        elif s[0]=='+':
            i +=1
        result = 0
        while i<len(s) and s[i].isdigit():
            result = result *10 +int(s[i])
            i +=1
        result *=sign
        
        INT_MIN = -2**31
        INT_MAX= 2**31-1
        
        return max(INT_MIN,min(result,INT_MAX))
    
        