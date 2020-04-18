# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            start_index = nums2.index(num1)
            found = False
            for i in range(start_index + 1, len(nums2)):
                if nums2[i] > num1:
                    found = True
                    result.append(nums2[i])
                    break
            if not found:
                result.append(-1)
        return result
                    
        
