class Solution:
    def largestSwap(self, s):
        #code here
        arr=list(s)
        n=len(arr)
        
        max_idx=[0]*n
        max_idx[-1]=n-1
        
        for i in range(n-2,-1,-1):
            if arr[i]>arr[max_idx[i+1]]:
                max_idx[i]=i
            else:
                max_idx[i]=max_idx[i+1]
        for i in range(n):
            if arr[max_idx[i]] != arr[i]:
                arr[i],arr[max_idx[i]]=arr[max_idx[i]],arr[i]
                break
        return "".join(arr)