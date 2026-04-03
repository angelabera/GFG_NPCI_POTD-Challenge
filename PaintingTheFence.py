class Solution:
    def countWays(self,n,k):
        #code here.
        if k==1 and n>2:
            return 0
        if n==1:
            return k
        e=1
        a=k*k
        for i in range(3, n+1):
            a1=a*k
            a1=a1-e*k
            e=a//k-e
            a=a1
        return a