#https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        word_len = len(A[0])
        indices_to_remove = set()
        for i in range(word_len):
            for j in range(len(A) - 1):
                if A[j][i] > A[j + 1][i]:
                    indices_to_remove.add(i)
                    break
        return len(indices_to_remove)
        
