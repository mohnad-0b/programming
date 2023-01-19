class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
      
      flips = []

      n = int("1"*len(s),2)      
      num = int(s,2)    
    
      for i in range(len(s)+1):
        flips.append((n^num).bit_count())
        n = n >> 1
  
      return min(flips)
