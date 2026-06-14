class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i,j in pre:
            adj[i].append(j)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED]*numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False
            
            states[node] = VISITING

            for n in adj[node]:
                if not dfs(n): return False
            
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if states[i] == UNVISITED:
                if not dfs(i): return False
            
        return True






