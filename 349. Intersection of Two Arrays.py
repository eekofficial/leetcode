#https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums_dict1 = collections.defaultdict(int)
        nums_dict2 = collections.defaultdict(int)
        min_n = min(len(nums1), len(nums2))
        max_n = max(len(nums1), len(nums2))
        i = 0
        while i < min_n:
            nums_dict1[nums1[i]] = True
            nums_dict2[nums2[i]] = True
            i += 1
        i = min_n
        if len(nums2) == max_n:
            while i < max_n:
                nums_dict2[nums2[i]] = True
                i += 1
            for k in nums_dict2.keys():
                if nums_dict1.get(k):
                    intersection.append(k)
        else:
            while i < max_n:
                nums_dict1[nums1[i]] = True
                i += 1
            for k in nums_dict1.keys():
                if nums_dict2.get(k):
                    intersection.append(k)
        return intersection
