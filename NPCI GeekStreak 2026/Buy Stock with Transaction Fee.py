class Solution:
    def maxProfit(self,arr,k):
        #Code here
        dp0=0
        dp1 = -arr[0]
        
        for price in arr[1:]:
            dp0=max(dp0,dp1+price-k)
            dp1=max(dp1,dp0-price)
        return dp0