#https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        first_num = ''.join([str(num) for num in A])
        return list(str(int(first_num) + K))
