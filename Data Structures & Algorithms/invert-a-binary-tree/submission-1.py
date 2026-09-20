# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Caso base en que la raiz es nula
        if root is None:
            return None
        
        #Invertir recursivamente los subarboles izqu y derecho
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        #Hacer swap
        root.left = right_inverted
        root.right = left_inverted

        #regresar la raiz
        return root