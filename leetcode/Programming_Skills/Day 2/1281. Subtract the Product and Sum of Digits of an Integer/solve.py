class Solution:
    
    def mult(self, ns: str) -> int:
        mult = 1
        for n in ns :
            mult *= int(n)
        return mult
    def sum(self, ns: str) -> int:
        sum = 0
        for n in ns:
            sum += int(n)
        return sum
    
    def subtractProductAndSum(self, n: int) -> int:
    
        return self.mult(str(n)) - self.sum(str(n))