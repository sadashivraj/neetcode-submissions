class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for i in prerequisites:
            adj[i[1]].append(i[0])

        visited = set()
        path = set()

        course_order = []


        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, visited, path, course_order, adj): return []

        return course_order[::-1]
        

def dfs(i, visited, path, course_order, adj):
    if i in path:
        return False
    if i in visited:
        return True

    visited.add(i)
    path.add(i)

    for neighbor in adj[i]:
        if not dfs(neighbor, visited, path, course_order, adj): return False
    course_order.append(i)
    path.remove(i)
    return True