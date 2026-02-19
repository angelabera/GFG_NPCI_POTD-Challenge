import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public ArrayList<Integer> missingRange(int[] arr, int low, int high) {
        ArrayList<Integer> ans=new ArrayList<>();
        HashSet<Integer> set=new HashSet<>();
        for(int i : arr) set.add(i);
        
        for(int i=low;i<=high;i++){
            if(set.contains(i)==false) ans.add(i);
        }
        
        return ans;
    }
}