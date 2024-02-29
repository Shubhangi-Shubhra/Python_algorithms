# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        left_values = self.preorderTraversal(root.left)
        current_value = [root.val]
        right_values = self.preorderTraversal(root.right)
        result = current_value + left_values +  right_values
        return result
        

class Solution(object):
    def inorderTraversal(self, root):
       
        if not root:
            return []
        left_values = self.inorderTraversal(root.left)
        current_value = [root.val]
        right_values = self.inorderTraversal(root.right)
        result = left_values + current_value + right_values
        return result
