class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, low, high):
            if not root:
                return True
            
            if not (low < root.val < high):
                return False
            
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

        return dfs(root, float('-inf'), float('inf'))