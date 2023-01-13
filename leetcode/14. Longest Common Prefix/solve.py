class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = min([len(s) for s in strs])
        
        ans = ""

        for j in range(i):
          c = strs[0][j]
          # print(c)
          for k in strs:
            if k[j] != c:
             return ans
          ans += strs[0][j]
        return ans 
