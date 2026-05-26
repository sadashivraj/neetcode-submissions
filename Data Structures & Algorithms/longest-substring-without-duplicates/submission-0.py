class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,length = 0,0

        counter = set()

        for R in range(len(s)):
            while s[R] in counter:
                counter.remove(s[L])
                L+=1
            counter.add(s[R])
            length = max(R-L+1, length)
        return length
            
            



        
        