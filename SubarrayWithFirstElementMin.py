class Solution:
    def countSubarrays(self, arr):
        #code here
        stack = []
        cnt = 0
        for e in arr:
            while stack and stack[-1] > e:
                stack.pop()
            stack.append(e)
            cnt += len(stack)
        return cnt