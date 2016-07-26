# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def get_depth(self, A):
    	if A is None:
    		return 0
    	else:
	    	return max(1 + self.get_depth(A.left), 1 + self.get_depth(A.right))

    def check(self, A):
    	left_depth = self.get_depth(A.left)
    	right_depth = self.get_depth(A.right)

    	if abs(left_depth - right_depth) > 1:
    		return 0

    	if A.left is not None:
    		if self.check(A.left) == 0:
    			return 0

    	if A.right is not None:
    		if self.check(A.right) == 0:
    			return 0

    	return 1

    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
    	print self.check(A)	


node = TreeNode(1)
node.left = TreeNode(0)
node.right = TreeNode(2)
node.right.right = TreeNode(3)
node.right.right.right = TreeNode(4)

Solution().isBalanced(node)