class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0,nums)

    def helper(self,i, nums):
        if i == len(nums):
            return [[]]
        
        result = []
        perms = self.helper(i+1, nums)
        for p in perms:
            for j in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(j, nums[i])
                result.append(pcopy)
        
        return result
        