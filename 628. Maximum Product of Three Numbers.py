#https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums) -> int:
        first_minimum = float('inf')
        second_minimum = float('inf')
        first_maximum = -float('-inf')
        second_maximum = -float('inf')
        third_maximum = -float('inf')
        for i in range(len(nums)):
            if nums[i] < second_minimum:
                first_minimum = second_minimum
                second_minimum = nums[i]
            elif nums[i] < first_minimum:
                first_minimum = nums[i]
            if nums[i] > third_maximum:
                first_maximum = second_maximum
                second_maximum = third_maximum
                third_maximum = nums[i]
            elif nums[i] > second_maximum:
                first_maximum = second_maximum
                second_maximum = nums[i]
            elif nums[i] > first_maximum:
                first_maximum = nums[i]
        
        positive_product = first_maximum * second_maximum * third_maximum
        negative_product = first_minimum * second_minimum * third_maximum 
        if negative_product > positive_product:
            return negative_product
        return positive_product
            
