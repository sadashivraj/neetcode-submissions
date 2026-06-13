class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')

        def dfs(node):
            nonlocal maxsum
            if not node:
                return 0
            
            leftsum = max(dfs(node.left), 0)
            rightsum = max(dfs(node.right), 0)
            
            current_path_sum = node.val + leftsum + rightsum
            maxsum = max(maxsum, current_path_sum)
            
            return node.val + max(leftsum, rightsum)
        
        dfs(root)
        return maxsum