class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):

            return False
        dict1 = {}
        dict2 = {}

        for k in range(len(s)):
            dict1[s[k]] = 1 + dict1.get(s[k], 0)
            dict2[t[k]] = 1 + dict2.get(t[k], 0)

        return dict1 == dict2

        