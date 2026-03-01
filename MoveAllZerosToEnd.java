class Solution {
    void pushZerosToEnd(int[] arr) {
        int j = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                if (i != j) {
                    arr[i] = arr[i] ^ arr[j];
                    arr[j] = arr[i] ^ arr[j];
                    arr[i] = arr[i] ^ arr[j];
                }
                j++;
            }
        }
    }
}