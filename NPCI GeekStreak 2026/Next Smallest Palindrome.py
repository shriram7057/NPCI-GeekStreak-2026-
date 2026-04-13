class Solution:
    def nextPalindrome(self, num):
        # code here
        n = len(num)
        if all(x == 9 for x in num):
            return [1] + [0]*(n-1) + [1]
        res = num[:]
        mid = n // 2
        i = mid -1
        j = mid + 1 if n %2 else mid
        while i >= 0:
            res[j] = res[i]
            i -= 1
            j += 1
        if res > num:
            return res
        carry = 1
        i = mid - 1
        
        if n % 2 == 1:
            res[mid] += carry
            carry = res[mid] // 10 
            res[mid] %= 10
            j = mid + 1
        else:
            j = mid 
        while i >= 0 and carry:
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
            res[j] = res[i]
            i -= 1
            j += 1
        return res
        