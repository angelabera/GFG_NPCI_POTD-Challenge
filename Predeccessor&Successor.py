class Solution:
    def findPreSuc(self, root, key):
        pred = None
        succ = None
        
        curr = root
        
        while curr:
            if curr.data < key:
                pred = curr
                curr = curr.right
            elif curr.data > key:
                succ = curr
                curr = curr.left
            else:
                # predecessor = max in left subtree
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    pred = temp
                
                # successor = min in right subtree
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    succ = temp
                break
        
        return pred, succ 