class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for i,j in zip(s,t):
            map_s[i] = 1+ map_s.get(i, 0)
            map_t[j] = 1+ map_t.get(j, 0)

        for i in map_s:
            if map_s[i] != map_t.get(i, -1):
                return False
        return True


        