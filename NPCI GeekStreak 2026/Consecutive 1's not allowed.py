class Solution:
	def countStrings(self,n):
    	# code here
    	if n == 0:
    	    return 1
    	dp0 = 1 
    	dp1 = 1
    	
    	for _ in range(2,n+1):
    	    new_dp0 = dp0 + dp1
    	    new_dp1 = dp0
    	    dp0 , dp1 = new_dp0,new_dp1
    	return dp0 + dp1
    	