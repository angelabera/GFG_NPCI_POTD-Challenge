class Solution {
    public int findMinDiff(ArrayList<Integer> arr, int m) {
        Collections.sort(arr);
        int start=0,end=m-1;
        int ans=Integer.MAX_VALUE;
        while(end<arr.size()){
            ans=Math.min(ans,(arr.get(end)-arr.get(start)));
            start++;
            end++;
        }
        return ans;
    }
}