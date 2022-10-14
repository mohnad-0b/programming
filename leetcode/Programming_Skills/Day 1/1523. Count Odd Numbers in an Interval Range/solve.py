class Solution:
    def countOdds(self, low: int, high: int) -> int:

        OddNumber = 0

        if (high%2 != 0 or low%2 != 0) :
            OddNumber = 1

        OddNumber += (high - low)//2
        return  OddNumber