class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums : 
            if i == 0:
                nums.append(0)
                nums.remove(0)