class Solution 
{
    public boolean isPossible(int h,int[] arr)
    {
        int count=0;
        for(int i:arr)if(i>=h)count++;
        return count>=h;
    }
    public int hIndex(int[] citations) {
        // code here
        int result=-1;
        int si=0;
        int ei=0;
        for(int i:citations)ei=Math.max(ei,i);
        
        while(si<=ei)
        {
            int mid=si+(ei-si)/2;
            
            if(isPossible(mid,citations))
            {
                result=mid;
                si=mid+1;
            }
            else ei=mid-1;
        }
        return result;
    }
}