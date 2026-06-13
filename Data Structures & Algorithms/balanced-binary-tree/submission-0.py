class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            
            heightl = dfs(node.left)
            heightr = dfs(node.right)
        
            if heightl is False or heightr is False or abs(heightl - heightr) > 1:
                return False
            return 1 + max(heightl, heightr)
        
        return dfs(root) is not False