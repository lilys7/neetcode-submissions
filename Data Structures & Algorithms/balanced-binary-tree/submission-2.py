# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #gotta implement dfs on the left and right subtrees and see if the diff between the two heights is greater than one
        def dfs(curr):
            if curr is None:
                return 0
            left = dfs(curr.left)
            if left == -1:
                return -1
            
            right = dfs(curr.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            return 1 + max(right, left)

        
        return dfs(root) != -1