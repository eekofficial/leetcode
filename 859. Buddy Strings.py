#https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        A = list(A)
        B = list(B)
        indexes = collections.defaultdict(list)
        not_equal_i = []
        duplicate = None
        for i in range(len(A)):
            if A[i] != B[i]:
                not_equal_i.append(i)
            else:
                indexes[A[i]].append(i)
                if len(indexes[A[i]]) >= 2:
                    duplicate = A[i]
        if len(not_equal_i) == 2:
            A[not_equal_i[0]], A[not_equal_i[1]] = A[not_equal_i[1]], A[not_equal_i[0]]
            if A == B:
                return True
            else:
                return False
        elif A == B and duplicate:
            return True
        else:
            return False
                
