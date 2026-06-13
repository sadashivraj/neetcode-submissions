# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])

        def bfs(node, queue):
            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    curr_node = queue.popleft()
                    if i == 0:
                        res.append(curr_node.val)
                    if curr_node.right:
                        queue.append(curr_node.right)
                    if curr_node.left:
                        queue.append(curr_node.left)

        bfs(root, queue)
        return res