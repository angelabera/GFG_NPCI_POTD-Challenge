class Solution:    
    def findUnion(self, a, b):
        u = sorted(set(list(a) + list(b)))
        return u