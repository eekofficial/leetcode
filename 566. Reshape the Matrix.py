#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])
        
        if n * m != r * c:
            return nums
        nums_row = []
        for i in range(n):
            for j in range(m):
                nums_row.append(nums[i][j])
        
        i = 0
        new_nums = [[nums_row[0]]]
        for j in range(1, len(nums_row)):
            if j % c == 0:
                new_nums.append([])
                i += 1
                new_nums[i].append(nums_row[j])
            else:
                new_nums[i].append(nums_row[j])
        return new_nums
                    
