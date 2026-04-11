class Solution:
    def countIncreasing(self, arr):
        # code here.
        n = len(arr)
        count = 0
        length = 1
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                length += 1
            else:
                count += (length *(length-1)) //2
                length = 1
        count += (length*(length-1)) //2
        return count