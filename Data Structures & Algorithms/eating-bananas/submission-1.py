import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        def calculate_hours(piles, k):
            if k == 0: return float('inf')
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours


        l = 1
        r = max(piles)
        while l <= r:
            mid = (l+r)//2
            total_hours = calculate_hours(piles,mid)
            if total_hours > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res
