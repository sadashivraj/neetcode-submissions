class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pqueue = deque([p])
        qqueue = deque([q])

        while pqueue and qqueue:
            for _ in range(len(pqueue)):
                nodeP = pqueue.popleft()
                nodeQ = qqueue.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                pqueue.append(nodeP.left)
                pqueue.append(nodeP.right)
                qqueue.append(nodeQ.left)
                qqueue.append(nodeQ.right)
        
        return True