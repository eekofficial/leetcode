# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        score_sorted = sorted([(nums[i], i) for i in range(len(nums))], key=lambda score: score[0], reverse=True)
        for i in range(len(score_sorted)):
            if i == 0:
                nums[score_sorted[i][1]] = "Gold Medal"
            elif i == 1:
                nums[score_sorted[i][1]] = "Silver Medal"
            elif i == 2:
                nums[score_sorted[i][1]] = "Bronze Medal"
            else:
                nums[score_sorted[i][1]] = str(i + 1)
        return nums
        
