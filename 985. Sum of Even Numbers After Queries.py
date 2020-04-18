#https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A, queries):
        result = [0] * len(queries)
        sum_of_evens = 0
        for num in A:
            if num % 2 == 0:
                sum_of_evens += num
        for i in range(len(queries)):
            query = queries[i]
            if A[query[1]] % 2 == 0:
                sum_of_evens -= A[query[1]]
                A[query[1]] += query[0]
                if A[query[1]] % 2 == 0:
                    sum_of_evens += A[query[1]]
            else:
                A[query[1]] += query[0]
                if A[query[1]] % 2 == 0:
                    sum_of_evens += A[query[1]]
            result[i] = sum_of_evens
        return result
