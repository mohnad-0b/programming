class Solution:
    def romanToInt(self, s: str) -> int:
        num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        Snum = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        res = 0
        i=0

        while i != len(s):
            
            if i+1 < len(s) and (s[i] + s[i+1]) in Snum : 
                print(s[i] + s[i+1],Snum[s[i] + s[i+1]],i)

                res += Snum[s[i] + s[i+1]]
                i += 2
            else : 
                print(s[i],num[s[i]],i)

                res += num[s[i]]
                i += 1
        return res
