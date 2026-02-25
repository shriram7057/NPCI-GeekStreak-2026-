class Solution {
    public int longestSubarray(int[] arr, int k) {
        // Code Here
        int n = arr.length;
        
        int[]a = new int[n];
        for (int i= 0;i<n;i++)
        {
            a[i] = (arr[i] > k) ? 1 : -1;
        }
        int[] pre= new int[n+1];
        for (int i = 0; i < n; i++)
        {
            pre[i+1] = pre[i] +a[i];
        }
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        for(int i = 0;i <= n; i++)
        {
            if(stack.isEmpty() || pre[i] < pre[stack.peek()])
            {
                stack.push(i);
            }
        }
        int ans = 0;
        for( int i=n;i>=0;i--)
        {
            while(!stack.isEmpty() && pre[i] > pre[stack.peek()])
            {
                ans = Math.max(ans,i - stack.peek());
                stack.pop();
            }
        }
        return ans;
    }
}
