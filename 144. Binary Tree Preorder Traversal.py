#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if not root:
            return nodes
        self.pre_order(root, nodes)
        return nodes
    
    def pre_order(self, root, nodes):
        nodes.append(root.val)
        if root.left:
            self.pre_order(root.left, nodes)
        if root.right:
            self.pre_order(root.right, nodes)
        
        
