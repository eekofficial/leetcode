#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = dict()
        for n in nums:
            if elements.get(n):
                return True
            else:
                elements[n] = True
        return False
