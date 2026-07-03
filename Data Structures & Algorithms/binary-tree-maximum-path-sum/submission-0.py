# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # node could be < 0
            # if it's smaller than 0, replace it with 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # as a reflection point having both left and right
            self.res = max(self.res, node.val + left + right)

            # if not a reflection pointer, have to pick a one
            return node.val + max(left, right)
        dfs(root)
        return self.res