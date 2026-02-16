class Solution:
    def minTime (self, arr, k):
        n = len(arr)
        
        if k >= n:
            return max(arr)
        
        
        low = max(arr)       
        high = sum(arr)       
        
        while low < high:
            mid = (low + high) // 2
            
            
            painters = 1
            total = 0
            
            for length in arr:
                total += length
                if total > mid:
                    painters += 1
                    total = length
            
            if painters <= k:
                high = mid
            else:
                low = mid + 1
        
        return low