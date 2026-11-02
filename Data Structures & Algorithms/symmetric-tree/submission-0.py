# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(node1, node2):
            if node1 is None or node2 is None:
                return node1 is node2
            return node1.val == node2.val and symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
        return symmetric(root.left, root.right)