# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.max_depth = 0
        
    def recurse(self, root, depth):
        if root.left is None and root.right is None:
            depth += 1
            if depth > self.max_depth:
                self.max_depth = depth

        if root.left is not None:
            self.recurse(root.left, depth + 1)
        
        if root.right is not None:
            self.recurse(root.right, depth + 1)


    def maxDepth(self, A):
        self.recurse(A, 0)
        return self.max_depth

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

print Solution().maxDepth(root)
