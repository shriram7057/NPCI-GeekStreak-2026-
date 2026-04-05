class Solution:
    def totalWays(self, arr, target):
        # code here
        total = sum(arr)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0 
        s = (total + target) // 2
        dp = [0] * (s+1)
        dp[0] = 1
        for num in arr:
            for j in range(s, num - 1 , -1 ):
                
                dp[j] += dp[j-num]
        return dp[s]