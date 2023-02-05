class Solution(object):
    def findAnagrams(self, s, p):
        n1 = Counter("abcdefghijklmnopqrstuvwxyz")
        n2 = Counter("abcdefghijklmnopqrstuvwxyz")
        l1 = len(p)
        l2 = len(s)      
        
        for i in "abcdefghijklmnopqrstuvwxyz" :
            n1[i] = 0
            n2[i] = 0
        
        
        for i,j in Counter(p).items():
            n1[i] = j

        
        for i,j in Counter(s[:l1]).items():
            n2[i] = j

        ans = []
        for i in range(l1,l2):  
            if n1 == n2:
                ans.append(i-l1)
            n2[s[i]] += 1
            n2[s[i-l1]] -= 1
        if n1 == n2:
            ans.append(l2-l1)
        return ans
