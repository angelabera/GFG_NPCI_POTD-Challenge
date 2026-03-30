import heapq
class Solution:
    def minCost(self, houses):
        visited=set()
        n=len(houses)
        arr=[(0,0)]
        total=0
        
        while len(visited)<n:
            cost,node=heapq.heappop(arr)
            
            if node in visited:
                continue
            
            total+=cost
            visited.add(node)
            
            for i in range(n):
                if i not in visited:
                    x1,y1=houses[node]
                    x2,y2=houses[i]
                    
                    dist=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(arr,(dist,i))
            
        
        return total