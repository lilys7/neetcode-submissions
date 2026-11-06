# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        res = defaultdict(list)
        def recurseDown(root, currHeight):
            if not root:
                return 
            res[currHeight].append(root.val)
            recurseDown(root.left, currHeight + 1)
            recurseDown(root.right, currHeight + 1)
        
        recurseDown(root, 0)
        return list(res.values())

        
        
        