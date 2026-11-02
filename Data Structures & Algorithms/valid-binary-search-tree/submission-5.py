# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = float('inf')
        if root is None:
            return True 
        
        def validate(node, left=-inf, right=inf):
            if node is None:
                return True 
            x = node.val
            return left < x < right and validate(node.left, left, node.val) and \
            validate(node.right, node.val, right)
        return validate(root) 