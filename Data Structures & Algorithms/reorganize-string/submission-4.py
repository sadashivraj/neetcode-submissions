class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-1*count, letter) for letter, count in counts.items()]
        heapq.heapify(heap)
        q = deque()
        res = []
        time = 0
        while heap or q:
            if heap:
                count, letter = heapq.heappop(heap)
                cnt = count + 1
                res.append(letter)
                if cnt != 0:
                    q.append((cnt, letter, time+2))
            else:
                # If the heap is empty but the queue isn't, it's impossible to continue
                return ""
            time += 1
            if q and q[0][2] <= time:
                item = q.popleft()
                heapq.heappush(heap, (item[0], item[1]))
        return ''.join(res) if len(res) == len(s) else ""