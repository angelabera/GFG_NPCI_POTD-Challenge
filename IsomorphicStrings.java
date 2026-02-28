class Solution {
    public boolean areIsomorphic(String s1, String s2) {
        char[] arr = new char[26];
        char[] arr1 = new char[26];
        
        for(int i = 0; i < s1.length(); i++){
            char ch1 = s1.charAt(i);
            char ch2 = s2.charAt(i);
            
            if(arr[ch1 - 'a' ] == '\u0000'){
                if(arr1[ch2 - 'a'] == '\u0000'){
                    arr1[ch2 - 'a'] = ch1;
                    arr[ch1 - 'a'] = ch2;
                }else{
                    return false;
                }
            }else{
                if(ch2 != arr[ch1 - 'a']){
                    return false;
                }
            }
        }
        return true;
    }
}