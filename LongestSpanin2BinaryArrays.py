class Solution:
    def equalSumSpan(self, a1, a2):
        diff = [a1[i]-a2[i] for i in range(len(a1))]
        max_sum = 0
        prefix_sum = 0
        first_sum = {}
        if len(a1) != len(a2):
            return 0
        for i in range(len(a1)):
            prefix_sum += diff[i]
            
            if prefix_sum == 0:
                max_sum = i+1
            
            if prefix_sum in first_sum:
                max_sum = max(max_sum, i-first_sum[prefix_sum])
            else:
                first_sum[prefix_sum] = i
        return max_sum