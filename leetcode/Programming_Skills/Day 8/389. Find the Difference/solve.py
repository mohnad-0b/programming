class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = sorted(t)
        s = sorted(s)

        for i in range(len(t)):
            if str(s[i:]).find(t[i]) == -1:
                return t[i]