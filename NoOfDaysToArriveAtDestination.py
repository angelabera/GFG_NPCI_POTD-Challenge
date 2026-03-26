from collections import defaultdict
import heapq
class Solution:
    def countPaths(self, V, edges):
        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
            
        dist = [float('inf')]*V
        ways = [0]*V
        
        # weight, node
        min_heap = [(0, 0)]
        dist[0] = 0
        ways[0] = 1
        
        while min_heap:
            wt, node = heapq.heappop(min_heap)
            
            if wt > dist[node]:
                continue
            
            for nbr, w in adjList[node]:
                new_wt = wt+w
                if new_wt < dist[nbr]:
                    dist[nbr] = new_wt
                    ways[nbr] = ways[node]
                    heapq.heappush(min_heap, (new_wt, nbr))
                elif new_wt == dist[nbr]:
                    ways[nbr] += ways[node]
        return ways[V-1]