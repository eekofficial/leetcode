# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = collections.defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        longest = 0
        for num in nums:
            if nums_dict[num - 1]:
                a = nums_dict[num] + nums_dict[num - 1]
                if a > longest:
                    longest = a
            if nums_dict[num + 1]:
                b = nums_dict[num] + nums_dict[num + 1]
                if b > longest:
                    longest = b
        return longest
