# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if not root:
            return nodes
        self.in_order(root, nodes)
        return nodes
    def in_order(self, root, nodes):
        if root.left:
            self.in_order(root.left, nodes)
        nodes.append(root.val)
        if root.right:
            self.in_order(root.right, nodes)
    
