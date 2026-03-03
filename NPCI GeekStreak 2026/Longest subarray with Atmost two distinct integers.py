class Solution:
    def totalElements(self, arr):
        # Code here
        left = 0
        freq = {}
        max_len = 0
        
        for right in range(len(arr)):
            freq[arr[right]] = freq.get(arr[right],0) + 1
            
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            max_len = max(max_len,right - left + 1)
        return max_len