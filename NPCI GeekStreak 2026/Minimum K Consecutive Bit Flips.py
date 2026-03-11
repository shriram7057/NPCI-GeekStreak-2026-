class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n=len(arr)
        flip=0
        res=0
        diff=[0]*(n+1)
        
        for i in range(n):
            flip ^= diff[i]
            
            if arr[i] ^ flip==0:
                if i + k > n:
                    return -1
                res += 1
                flip ^= 1
                diff[i+k] ^= 1
        return res