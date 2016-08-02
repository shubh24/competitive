# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer

    def __init__(self):
        self.count = 0

    def recurse(self, root, k):
        if self.count == k:
            return (True, root.val)

        if root.left is None:
            self.count += 1
            if self.count == k:
                return (True, root.val)

            if root.right is None:
                return (False, -1)

            else:
                res = self.recurse(root.right, k)
                if res[0] == True:
                    return res
        else:
            res = self.recurse(root.left, k)       
            if res[0] == True:
                return res
    
            self.count += 1
            if self.count == k:
                return (True, root.val)

            if root.right is not None:
                res = self.recurse(root.right, k)
                if res[0] == True:
                    return res

    def kthsmallest(self, root, k):
        res = self.recurse(root, k)
        if res[0] == True:
            return res[1]

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)


print Solution().kthsmallest(root, 4)