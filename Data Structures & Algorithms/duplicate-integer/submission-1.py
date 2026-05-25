class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for i in nums:
            if i in cache:
                return True
            else:
                cache[i] = 1
        return False
