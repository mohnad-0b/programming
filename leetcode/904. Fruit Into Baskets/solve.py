class Solution(object):
    def totalFruit(self, fruits):
        anss = []
        ht,ans,l = Counter(),0,0
        for r in fruits:
            ht[r] += 1
            ans += 1
            while len(ht) > 2:
                ht[fruits[l]] -= 1
                ans -=1
                if not ht[fruits[l]] :
                    ht.pop(fruits[l])
                l += 1
            anss.append(ans)
        return max(anss)
