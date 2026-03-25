from collections import deque

class Solution:
    def minHeightRoot(self, V, edges):
        
        # Edge case
        if V == 1:
            return [0]
        
        # Build graph
        adj = [[] for _ in range(V)]
        degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Find initial leaves
        leaves = deque()
        for i in range(V):
            if degree[i] == 1:
                leaves.append(i)
        
        remaining_nodes = V
        
        # Remove leaves layer by layer
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)