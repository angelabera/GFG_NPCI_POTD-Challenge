class Solution:
    def articulationPoints(self, V, edges):
        # Step 1: Build the Adjacency List
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Initialize arrays for Tarjan's Algorithm
        visited = [False] * V
        tin = [-1] * V
        low = [-1] * V
        mark = [False] * V # Handles duplicates if a node is an AP for multiple subtrees
        self.timer = 0
        
        # Step 3: Define the DFS logic
        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1
            children = 0
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue # Don't go back the way we came
                    
                if not visited[neighbor]:
                    children += 1
                    dfs(neighbor, node)
                    
                    # On callback, update the low value of current node
                    low[node] = min(low[node], low[neighbor])
                    
                    # Check Case 2: Non-root Articulation Point condition
                    if parent != -1 and low[neighbor] >= tin[node]:
                        mark[node] = True
                else:
                    # Back-edge found. Update the low value.
                    low[node] = min(low[node], tin[neighbor])
            
            # Check Case 1: Root Articulation Point condition
            if parent == -1 and children > 1:
                mark[node] = True

        # Step 4: Run DFS for all components (handles disconnected graphs)
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
                
        # Step 5: Format the output
        ans = []
        for i in range(V):
            if mark[i]:
                ans.append(i)
                
        if not ans:
            return [-1]
            
        return ans