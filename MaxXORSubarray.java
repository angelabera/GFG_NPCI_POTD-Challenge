class Solution {
    public int maxSubarrayXOR(int[] arr, int k) {
        int windowXor = 0;
        int maxXor = 0;
        for(int i = 0; i < k;i++){
            windowXor = windowXor ^ arr[i];
        }
        maxXor = windowXor;
        for(int i = k;i < arr.length;i++){
            windowXor = windowXor ^ arr[i - k] ^ arr[i];
            maxXor = Math.max(maxXor,windowXor);
        }
        return maxXor;
        
    }
}