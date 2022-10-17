class Solution:

    def isHappy(self, n: int) -> bool:

        new_n1 = n
        s = []
        while True :
            new_n2 = 0
            for i in str(new_n1):
                new_n2 += int(i)**2
            if new_n2 == 1 :
                return True
            if new_n2 in s:
                return False
            else:
                s.append(new_n2)
                new_n1 = new_n2