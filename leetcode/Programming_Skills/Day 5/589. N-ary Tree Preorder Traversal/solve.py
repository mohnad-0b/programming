"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

"""

class Solution:
    def cheld(self,children,tree):
        for i in range(len(children)):
            tree.append(children[i].val)
            self.cheld(children[i].children,tree)
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root :
            return []
        tree = [root.val]
        
        self.cheld(root.children,tree)
            
        return tree