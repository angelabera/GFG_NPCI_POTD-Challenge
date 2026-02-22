class Solution {
    public long subarrayXor(int arr[], int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int prefixXor = 0;
        long count = 0;

        map.put(0, 1);

        for (int num : arr) {
            prefixXor ^= num;

            if (map.containsKey(prefixXor ^ k)) {
                count += map.get(prefixXor ^ k);
            }

            map.put(prefixXor, map.getOrDefault(prefixXor, 0) + 1);
        }

        return count;
    }
}