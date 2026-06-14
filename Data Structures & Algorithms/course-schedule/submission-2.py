from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in pre:
            graph[b].append(a)         
            indegree[a] += 1     
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1   
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return completed == numCourses