class Solution {
    public String largestSwap(String s) {
        int n = s.length();
        StringBuilder sb = new StringBuilder(s);
        int index1 = -1, index2 = -1;
        int i = n - 1;
        for(int j=n-1;j>=0;j--) {
            char ch1 = s.charAt(j);
            char ch2 = s.charAt(i);
            
            if(ch1>ch2) {
                i = j;
            } else if(ch1<ch2) {
                index1 = i;
                index2 = j;
            }
        }
        
        if(index1==-1)
            return sb.toString();
        
        char ch1 = sb.charAt(index1);
        char ch2 = sb.charAt(index2);
        sb.setCharAt(index1, ch2);
        sb.setCharAt(index2, ch1);
        return sb.toString();
    }
}