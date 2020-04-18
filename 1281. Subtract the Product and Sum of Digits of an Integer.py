#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0
        n = str(n)
        for i in n:
            product_of_digits *= int(i)
            sum_of_digits += int(i)
        return product_of_digits - sum_of_digits
