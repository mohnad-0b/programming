class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums :
            try : 
                s1 = nums.index(n)
                if  (target - n) == n :
                
                    e = (nums.index(target - n))
                    v = nums[e]
                    nums = nums[:e] + nums[e+1:]
                    
                    try:
                        s2 = nums.index(target - n) + 1
                    except ValueError:
                        nums = nums[:e] + [v] + nums[e:]
                        continue
                    solve = [s1,s2]
                    return solve

                else :
                    
                    s2 = nums.index(target - n)                    
                    solve = [s1,s2]
                    
                    return solve
                
            except ValueError:
                continue
