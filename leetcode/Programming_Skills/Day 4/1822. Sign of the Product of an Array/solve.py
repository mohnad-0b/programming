class Solution:
    def signFunc(self,x):
        if x > 0 :
            return 1
        else :
            return -1

    def arraySign(self, nums: List[int]) -> int:
        res = 1
        if 0 in nums :
            return 0
        else :
            for x in nums :
                res *= self.signFunc(x)
        return res
