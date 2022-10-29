# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        
        sumOfLeftLeaves = 0
        
        # Part One Of Code :
        
        if root.left != None :
            if (root.left).left == None and (root.left).right == None :
                sumOfLeftLeaves += (root.left).val
            else : 
                sumOfLeftLeaves += self.sumOfLeftLeaves(root.left)
        
        # Part Tow Of Code :
        
        if root.right != None :
            if (root.right).left != None or (root.right).right != None :
                sumOfLeftLeaves += self.sumOfLeftLeaves(root.right)
        return sumOfLeftLeaves