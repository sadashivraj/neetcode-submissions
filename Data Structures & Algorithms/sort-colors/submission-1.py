class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map = [0,0,0]
        for i in nums:
            map[i] = map[i]+1
        
        k = 0
        for i in range(3):
            while map[i]:
                map[i] -= 1
                nums[k] = i
                k+=1
                
        return nums

        