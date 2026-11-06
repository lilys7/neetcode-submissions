# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def traverseDown(root, upperMax):
            nonlocal total
            if not root:
                return
            if root.val >= upperMax:
                total += 1
            traverseDown(root.left, max(upperMax, root.val))
            traverseDown(root.right, max(upperMax, root.val))
        traverseDown(root, root.val)
        return total

