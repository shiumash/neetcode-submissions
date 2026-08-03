# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        1
    1       3
        2       4 
    
    11 + 132 + 134
    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return root.val
    

        def dfs(node, curSum):
            if not node:
                return 0
            curSum = curSum * 10 + node.val
            if not node.left and not node.right:
                return curSum
            return dfs(node.left, curSum) + dfs(node.right, curSum)
        
        return dfs(root, 0)