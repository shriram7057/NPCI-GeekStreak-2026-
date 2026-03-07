class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	n = len(arr)
    	
    	arr = [x*x for x in arr]
    	
    	s = set(arr)
    	
    	for i in range(n):
    	    for j in range(i+1,n):
    	        if arr[i] + arr[j] in s:
    	            return True
    	return False
    	 