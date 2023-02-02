class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = "0" + order
        for i in range(len(words)-1):
            if order.index(words[i][0]) < order.index(words[i+1][0]):
                continue 
            elif order.index(words[i][0]) == order.index(words[i+1][0]):
                
                if len(words[i]) > len(words[i+1]) : 
                    loop = len(words[i])
                    words[i+1] += "0"*(len(words[i]) - len(words[i+1]))
                else : 
                    loop = len(words[i+1])
                    words[i] += "0"*(len(words[i+1]) - len(words[i]))

                for l in range(loop) : 
                     print(words[i][l],words[i+1][l])
                     if order.index(words[i][l]) > order.index(words[i+1][l]):
                         return False
                     elif order.index(words[i][l]) < order.index(words[i+1][l]):
                         break
            else : 
                return False
        return True
        
