'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

from sklearn.base import defaultdict


class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
            
        hashmap = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            
            hashmap[level].append(node.data)
            
            if node.left:
                queue.append((node.left, level-1))
            if node.right:
                queue.append((node.right, level+1))
        
        res = [val for _, val in sorted(hashmap.items())]        
        return res