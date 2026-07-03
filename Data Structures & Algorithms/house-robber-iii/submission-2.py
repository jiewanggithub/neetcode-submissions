# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node, parent_robbed):
            if not node:
                return 0

            state = (node, parent_robbed)

            if state in memo:
                return memo[state]

            if parent_robbed:
                result = (
                    dfs(node.left, False)
                    + dfs(node.right, False)
                )
            else:
                rob = (
                    node.val
                    + dfs(node.left, True)
                    + dfs(node.right, True)
                )

                skip = (
                    dfs(node.left, False)
                    + dfs(node.right, False)
                )

                result = max(rob, skip)

            memo[state] = result
            return result

        return dfs(root, False)