# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        for number in range(left, right + 1):
            self_dividing = True
            num = number
            while num > 0:
                digit = num % 10
                if digit == 0 or number % digit != 0:
                    self_dividing = False
                num = num // 10
            if self_dividing:
                self_dividing_numbers.append(number)
        return self_dividing_numbers
                
            
