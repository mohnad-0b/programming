# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root == None :
            return 0
        
        rootL = self.maxDepth(root.left)
        rootR = self.maxDepth(root.right)
        # print(rootL,rootR)
        
        return max(rootL,rootR) + 1
