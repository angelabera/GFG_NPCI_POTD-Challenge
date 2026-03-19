class Solution:
    def largestBst(self, root):
        self.ans = 0
        
        def solve(node):
            if not node:
                return (float('inf'), float('-inf'), 0)
            
            lmin, lmax, lsize = solve(node.left)
            rmin, rmax, rsize = solve(node.right)
            
            if lmax < node.data < rmin:
                size = lsize + rsize + 1
                self.ans = max(self.ans, size)
                return (min(lmin, node.data), max(rmax, node.data), size)
            
            return (float('-inf'), float('inf'), max(lsize, rsize))
        
        solve(root)
        return self.ans