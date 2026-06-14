class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)
        maps1 = Counter(s1)

        while r <= len(s2):
            maps2 = Counter(s2[l:r])
            if maps1 == maps2:
                return True
            else:
                l += 1
                r += 1
        
        return False