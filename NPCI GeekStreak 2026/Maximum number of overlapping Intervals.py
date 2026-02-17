class Solution:
    def overlapInt(self, arr):
        # code here
        n = len(arr)
        start = []
        end = []
        
        for s , e in arr:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        
        i = j = 0
        curr = 0
        max_overlap = 0
        
        while i < n and j < n:
            if start[i] <= end[j]:
                curr += 1
                max_overlap = max(max_overlap,curr)
                i += 1
            else:
                curr -= 1
                j += 1
        return max_overlap      
                
