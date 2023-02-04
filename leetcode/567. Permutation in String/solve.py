class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = Counter(s1)
        l1 = len(s1)
        for i in range(l1,len(s2)+1):
            if n1 == Counter(s2[i-l1:i]):
                return True
        return False
