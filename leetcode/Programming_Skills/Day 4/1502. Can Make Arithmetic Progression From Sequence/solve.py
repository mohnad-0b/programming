class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        for i in range(len(arr)-2) :
            if (arr[i] - arr[i+1]) != (arr[i+1] - arr[i+2]):
                return False
            else :
                continue
        return True
