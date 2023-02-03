class Solution:
    def convert(self, s: str, numRows: int) -> str:

        ans = ['']*numRows
        cont = 0
        
        while True :
            
            for i in range(numRows) : 
                print(cont,i)
                ans[i] += s[cont]
                cont += 1
                if cont == len(s):
                    return "".join(ans)                    
            
            for i in range(numRows - 2,0,-1):
                print(cont,i)
                ans[i] += s[cont]
                cont += 1
                if cont == len(s):
                    return "".join(ans)
