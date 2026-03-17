'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import defaultdict,deque
class Solution:
    def minTime(self, root, target):
        # code here
        dic=defaultdict(list)
        def dfs(node):
            if node is None :
                pass
            if node.left:
                dic[node.data].append(node.left.data)
                dic[node.left.data].append(node.data)
                dfs(node.left)
            if node.right:
                dic[node.data].append(node.right.data)
                dic[node.right.data].append(node.data)
                dfs(node.right)
        dfs(root)
        visited=set()
        stack=deque()
        stack.extend(dic[target])
        visited.add(target)
        time=0
        while(stack):
            l=len(stack)
            j=0
            while(j<l):
                if stack[0] in visited:
                    stack.popleft()
                else:
                    visited.add(stack[0])
                    stack.extend(dic[stack[0]])
                    stack.popleft()
                j+=1
            time+=1
        if time==0:
            return 0
        return time-1