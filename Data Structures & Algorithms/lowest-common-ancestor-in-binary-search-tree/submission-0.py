class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_val, q_val = min(p.val, q.val), max(p.val, q.val)

        def dfs(node):
            if not node:
                return None

            if node.val > q_val:  
                return dfs(node.left)
            elif node.val < p_val: 
                return dfs(node.right)
            else:  
                return node

        return dfs(root)
