class Solution:
    def longestKSubstr(self, s, k):
        # code here
        left = 0
        freq = {}
        max_len = -1
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            
            while len(freq)>k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
        return max_len
        
        