class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        for i in nums1 : 
            for j in nums2[nums2.index(i):] :
                if j > i :
                    sol.append(j)
                    break
                if j == nums2[-1]:
                    sol.append(-1)
        return sol
