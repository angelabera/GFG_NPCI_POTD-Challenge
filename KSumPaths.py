'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def dfs (self, node, k, current_sum, prefix):
        if node is None:
            return 0
        current_sum += node.data
        
        count = prefix.get(current_sum - k, 0)
        
        prefix[current_sum] = prefix.get(current_sum, 0) + 1
        
        count += self.dfs(node.left, k, current_sum, prefix)
        count += self.dfs(node.right, k, current_sum, prefix)
        
        prefix[current_sum] -= 1
        
        return count
        
    def countAllPaths(self, root, k):
        prefix = {0:1}
        return self.dfs( root, k, 0, prefix)