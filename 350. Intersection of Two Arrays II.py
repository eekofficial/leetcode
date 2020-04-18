# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums_dict1 = dict()
        nums_dict2 = dict()
        min_n = min(len(nums1), len(nums2))
        max_n = max(len(nums1), len(nums2))
        for i in range(min_n):
            if nums_dict1.get(nums1[i]):
                nums_dict1[nums1[i]] += 1
            else:
                nums_dict1[nums1[i]] = 1
            if nums_dict2.get(nums2[i]):
                nums_dict2[nums2[i]] += 1
            else:
                nums_dict2[nums2[i]] = 1
        if len(nums1) == max_n:
            for i in range(min_n, max_n):
                if nums_dict1.get(nums1[i]):
                    nums_dict1[nums1[i]] += 1
                else:
                    nums_dict1[nums1[i]] = 1
            for i in nums_dict1.keys():
                if nums_dict2.get(i):
                    intersection += [i] * min(nums_dict1[i], nums_dict2[i])
        else:
            for i in range(min_n, max_n):
                if nums_dict2.get(nums2[i]):
                    nums_dict2[nums2[i]] += 1
                else:
                    nums_dict2[nums2[i]] = 1
            for i in nums_dict2.keys():
                if nums_dict1.get(i):
                    intersection += [i] * min(nums_dict1[i], nums_dict2[i])
        return intersection
