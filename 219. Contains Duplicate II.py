# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            if len(nums_dict[nums[i]]) == 0:
                nums_dict[nums[i]].append(i)
            else:
                for index in nums_dict[nums[i]]:
                    if abs(index - i) <= k:
                        return True
                nums_dict[nums[i]].append(i)
        return False
            
