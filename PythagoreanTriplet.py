class Solution:
    def pythagoreanTriplet(self, arr):
        MAX = 1000
        present = [False]*(MAX+1)
        for num in arr:
            present[num] = True
            
        for a in range(1, MAX+1):
            if not present[a]:
                continue
            
            for b in range(a+1, MAX+1):
                if not present[b]:
                    continue
                
                squared = (a*a+b*b)
                c = int(squared**0.5)
                if c <= MAX and c*c == squared and present[c]:
                    return True
        return False