class Solution(object):
    def addToArrayForm(self, num, k):
        s = "".join([str(i) for i in num])
        return [int(i) for i in str(int(s) + k)]
        
