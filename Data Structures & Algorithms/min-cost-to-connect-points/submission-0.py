class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cost(x1:int , y1:int, x2:int, y2:int):
            return abs(x1 - x2) + abs(y1 - y2)
        
        adj = defaultdict(list)
        visited = set()
        total_cost = 0
        minheap = []
        

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                adj[tuple(points[i])].append((cost(points[i][0], points[i][1], points[j][0], points[j][1]), tuple(points[j])))
                adj[tuple(points[j])].append((cost(points[i][0], points[i][1], points[j][0], points[j][1]), tuple(points[i])))
        
        visited.add(tuple(points[0]))
        for cost_val, neighbor in adj[tuple(points[0])]:
            heapq.heappush(minheap, (cost_val, neighbor))

        while len(visited) < len(points):
            cost_val, curr_point = heapq.heappop(minheap)
            if tuple(curr_point) in visited:
                continue
            
            total_cost += cost_val
            visited.add(tuple(curr_point))

            for next_cost, neighbor in adj[curr_point]:
                if tuple(neighbor) not in visited:
                    heapq.heappush(minheap, (next_cost, neighbor))

        return total_cost