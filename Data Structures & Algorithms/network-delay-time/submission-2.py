class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        shortest = {}

        for i in times:
            adj[i[0]].append((i[1], i[2]))
        
        minheap = [(0, k)]
        while minheap:
            weight, node = heapq.heappop(minheap)

            if node in shortest:
                continue
            shortest[node] = weight

            for neigh, neigh_weight in adj[node]:
                if neigh not in shortest:
                    heapq.heappush(minheap, (weight+neigh_weight, neigh))
            
        return max(shortest.values()) if len(shortest) == n else -1