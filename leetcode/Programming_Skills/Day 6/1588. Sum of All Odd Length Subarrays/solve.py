class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        for i in range(0,len(arr),2):
        
            for j in range(len(arr)):
                if i+1+j > len(arr):
                    break
                for k in arr[j:i+1+j]:
                    sum += k
                
        return sum