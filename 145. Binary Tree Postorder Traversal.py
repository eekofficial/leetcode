# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if not root:
            return nodes
        self.post_order(root, nodes)
        return nodes
        
    def post_order(self, root, nodes):
        if root.left:
            self.post_order(root.left, nodes)
        if root.right:
            self.post_order(root.right, nodes)
        nodes.append(root.val)
        
