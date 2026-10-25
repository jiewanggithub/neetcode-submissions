# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        
        def same(node, subroot):
            if not node and not subroot:
                return True
            if not node or not subroot:
                return False

            return (
                node.val == subroot.val
                and same(node.left, subroot.left)
                and same(node.right, subroot.right)
            )

        def dfs(node):
            if not node:
                return False 

            if same(node, subRoot):
                return True 

            return dfs(node.left) or dfs(node.right)
        return dfs(root)