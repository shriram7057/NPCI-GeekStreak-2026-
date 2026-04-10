class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        if n < 3:
            return []
                
        left_min = [-1]*n
        right_max = [-1]*n
        min_idx = 0
        for i in range(1,n):
            if arr[i] <= arr[min_idx]:
                min_idx = i
                left_min[i] = -1
            else:
                left_min[i] = min_idx
        max_idx = n - 1
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[max_idx]:
                max_idx = i
                right_max[i] = -1
            else:
                right_max[i] = max_idx
        for i in range(n):
            if left_min[i] != -1 and right_max[i] != -1:
                return [arr[left_min[i]],arr[i],arr[right_max[i]]]
        return []