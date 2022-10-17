class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        stop = 0
        for (i,j) in zip(s1,s2):
            if i not in s2 or j not in s1 or s1.count(i) != s2.count(i) or s1.count(j) != s2.count(j):
                print(s1.count(i),s2.count(j))
                return False
            if i != j:
                stop += 1
            if stop > 2 :
                print(stop)
                return False
        return True