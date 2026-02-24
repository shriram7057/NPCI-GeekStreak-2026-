class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        n = len(a1)
        diff_index={0: -1}
        max_len = 0
        prefix_diff = 0
        
        for i in range(n):
            prefix_diff += a1[i] - a2[i]
            
            if prefix_diff in diff_index:
                max_len = max(max_len,i - diff_index[prefix_diff])
            else:
                diff_index[prefix_diff] = i
        return max_len