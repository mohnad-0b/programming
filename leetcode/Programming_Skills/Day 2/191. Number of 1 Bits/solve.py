class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in str(bin(n))[2:]:
            # print(i,end="")
            if i == "1":
                ones += 1
        return ones