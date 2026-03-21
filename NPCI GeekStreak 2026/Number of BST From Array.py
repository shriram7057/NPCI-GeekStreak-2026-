class Solution:
    def countBSTs(self, arr):
        # Code here
        from functools import lru_cache
        @lru_cache(None)
        def count(nums):
            if len(nums) <= 1:
                return 1
            total = 0
            for i in range(len(nums)):
                root = nums[i]
                left = tuple(x for x in nums if x < root)
                right = tuple(x for x in nums if x > root)
                
                total += count(left) * count(right)
            return total
            
        res = []
        for root in arr:
            left = tuple(x for x in arr if x < root)
            right = tuple(x for x in arr if x > root)
            res.append(count(left) * count(right))
        return res
        