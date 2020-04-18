#https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        num_different = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                num_different += 1
        return num_different
        
