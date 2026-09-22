# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        def inorder_traversal(node):
            if not node:
                return 
            inorder_traversal(node.left)
            res.append(node.val)
            inorder_traversal(node.right)
            return 
        inorder_traversal(root)
        return res[k-1]