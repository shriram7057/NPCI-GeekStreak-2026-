class Solution:
    def minWindow(self, s, p):
        # code here
        from collections import Counter
        need = Counter(p)
        have = {}
        required= len(need)
        formed = 0
        
        left = 0
        min_len = float('inf')
        start = 0
        
        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c,0) + 1
            
            if c in need and have[c] == need[c]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                ch = s[left]
                have[ch] -= 1
                if ch in need and have[ch] < need[ch]:
                    formed -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[start:start + min_len]