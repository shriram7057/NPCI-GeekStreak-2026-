class Solution:
    def maxOnes(self, arr):
        # code here
        total_ones = sum(arr)
        max_gain = 0
        curr_gain = 0
        for x in arr:
            val = 1 if x == 0 else -1
            curr_gain = max(val,curr_gain + val)
            max_gain = max(max_gain,curr_gain)
        return total_ones + max_gain
        