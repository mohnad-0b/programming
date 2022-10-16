class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums ,reverse=True)
        while len(nums) >= 3 :
            if nums [0] + nums[1] > nums[2] :
                if nums [0] + nums[2] > nums[1] :
                    if nums [2] + nums[1] > nums[0] :
                        return nums[0] + nums[1] + nums[2]
            nums.remove(nums[0])
        return 0