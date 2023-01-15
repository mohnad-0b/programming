class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1 : return len(s)
        counts = []
        # c = "".join({key:valu for valu,key in enumerate(set(s))})
        
        for i in range(len(s)) :
          sub = s[i]  
          for j in range(i+1,len(s)) :
            if s[j] in sub : 
              break
            else : 
              sub += s[j]
          print(sub)
          counts.append(len(sub))
          sub = ""
          # if (len(sub) == 26) : return 26
        return max(counts) 
