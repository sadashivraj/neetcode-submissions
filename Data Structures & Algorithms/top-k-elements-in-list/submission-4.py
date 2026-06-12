import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        hashset = {}
        result = []

        for i in nums:
            hashset[i] = hashset.get(i, 0) + 1
        
        for key,v in hashset.items():
            heapq.heappush(maxheap, (-v,-key))

        while k > 0:
            result.append(-heapq.heappop(maxheap)[1])
            k-=1

        return result

        