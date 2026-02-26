class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        map1 = {}
        map2 = {}
        
        for c1, c2 in zip(s1, s2):
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                if c2 in map2:
                    return False
                map1[c1] = c2
                map2[c2] = c1
        
        return True