#https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        
        results = {}
        
        while q:     
            node, i = q.popleft()
            
            if i not in results:
                results[i] = []
            
            results[i].append(node.val)
            
            if node.left:
                q.append((node.left, i + 1))
            if node.right:
                q.append((node.right, i + 1))
        return [sum(level) / len(level) for level in results.values()]
            
        
    
