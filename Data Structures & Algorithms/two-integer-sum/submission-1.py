class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in maps:
                return [maps[diff], i]
            maps[val] = i
        
        
            
                


        