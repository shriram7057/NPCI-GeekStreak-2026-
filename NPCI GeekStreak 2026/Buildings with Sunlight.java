class Solution {
    public int visibleBuildings(int arr[]) {
        int count = 0;
        int maxHeight = 0;
        
        for (int h : arr) {
            if (h >= maxHeight) {
                count++;
                maxHeight = h;
            }
        }
        
        return count;
    }
}