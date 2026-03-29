class Solution:
    def countPartitions(self, arr, diff):
        s = sum(arr)
        if s < diff:
            return 0
            
        total = (s+diff)
        if total % 2 != 0:
            return 0
            
        target = total // 2
        
        cache = {}
        def f(idx, target):
            if idx >= len(arr):
                return 1 if target == 0 else 0
            
            if (idx, target) in cache:
                return cache[(idx, target)]
            
            not_take = f(idx+1, target)
            take = 0
            if arr[idx] <= target:
                take = f(idx+1, target-arr[idx])
            cache[(idx, target)] = take+not_take
            return cache[(idx, target)]
        return f(0, target)
