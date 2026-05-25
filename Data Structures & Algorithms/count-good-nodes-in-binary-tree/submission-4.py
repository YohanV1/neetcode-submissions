# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        c = 0
        def dfs(node, maxVal):
            nonlocal c
            if not node:
                return None

            if node.val >= maxVal:
                maxVal = node.val
                c+=1
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, -101)
        return c