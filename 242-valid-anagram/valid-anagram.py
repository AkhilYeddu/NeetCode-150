class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i in range(0, len(s)):
            map1[s[i]] = 1 + map1.get(s[i], 0)
            map2[t[i]] = 1 + map2.get(t[i], 0)
        
        for key in map1:
            if map1[key] != map2.get(key, 0):
                return False
        return True
        