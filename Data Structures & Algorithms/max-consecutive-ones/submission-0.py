class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        count=0
        for i in range(0,len(nums)):

            if nums[i]:
                count+=1
            else:
                if count>max:
                    max=count
                count=0
        if count>max:
            return count
        return max
        