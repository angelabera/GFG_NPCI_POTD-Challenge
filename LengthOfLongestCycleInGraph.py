class Solution:
    def longestCycle(self, V, edges):
        adj = [-1]* V
        for u,v in edges:
            adj[u] = v
        visited = [False] * V
        longest = -1
        
        for i in range(V):
            if visited[i]:
                continue
            
            curr = i
            step_map = {}
            step = 0
            
            while curr != -1 and not visited[curr]:
                visited[curr] = True
                step_map[curr] = step
                step += 1
                
                next_node = adj[curr]
                
                if next_node in step_map:
                    cycle_length = step - step_map[next_node]
                    longest = max(longest, cycle_length)
                    break
                
                curr = next_node
                
        return longest