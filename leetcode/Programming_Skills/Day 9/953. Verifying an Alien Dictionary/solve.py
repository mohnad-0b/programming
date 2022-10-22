class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order = "#"+order

        for i in range(len(words)-1):

            if len(words[i]) > len(words[i+1]) :
                words[i+1] += '#'
            elif len(words[i]) < len(words[i+1]) :
                words[i] += '#'

            for j in range(len(words[i+1])):
                print(order.find(words[i][j]),order.find(words[i+1][j])) 
                if order.find(words[i][j]) > order.find(words[i+1][j]):
                    return False
                elif order.find(words[i][j]) != order.find(words[i+1][j]):
                    break

        return True