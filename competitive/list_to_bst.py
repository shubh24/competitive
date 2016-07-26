# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def print_node(self, tree_node):
        print tree_node.val
        if tree_node.left is not None:
            self.print_node(tree_node.left)
        if tree_node.right is not None:
            self.print_node(tree_node.right)

    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        curr = A

        tree_node = TreeNode(A.val)

        while (curr.next):
            curr = curr.next
            traverse_tree_node = tree_node

            while (1):
                if traverse_tree_node is None:
                    curr_tree_node = TreeNode(curr.val)
                    if left_or_right == "left":
                        parent.left = curr_tree_node
                    else:
                        parent.right = curr_tree_node

                    break   

                elif curr.val <= traverse_tree_node.val:
                    parent = traverse_tree_node
                    left_or_right = "left"
                    traverse_tree_node = traverse_tree_node.left

                elif curr.val > node.val:
                    parent = traverse_tree_node
                    left_or_right = "right"                    
                    traverse_tree_node = traverse_tree_node.right

        self.print_node(tree_node)


node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(2)
node.next.next.next = ListNode(-1)

    
Solution().sortedListToBST(node)