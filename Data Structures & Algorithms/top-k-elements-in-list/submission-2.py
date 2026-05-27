class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = {}
        # freq = [[] for _ in range(len(nums) + 1)]
        
        # for n in nums:
        #     counter[n] = counter.get(n,0) + 1
        # for n,c in counter.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        counter = {}
        for x in nums: counter[x] = counter.get(x, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        q = []
        for number, count in counter.items():
            heapq.heappush(q, -1*(count))
            freq[count].append(number)

        res = []
        while k > 0:
            count = -heapq.heappop(q)
            if freq[count]:
                res.append(freq[count].pop())
                k-=1
        return res


        