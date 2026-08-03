# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (node.val > low and node.val < high):
                return False
            left_val = dfs(node.left, low, node.val)
            right_val = dfs(node.right, node.val, high)

            return left_val and right_val
        
        return dfs(root, float('-inf'), float('inf'))
            