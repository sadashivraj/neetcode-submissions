class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for i,j in zip(s,t):
            map_s[i] = 1+ map_s.get(i, 0)
            map_t[j] = 1+ map_t.get(j, 0)

       
        return map_s == map_t


        