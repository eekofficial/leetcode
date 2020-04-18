#https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr = sorted([[arr[i], i] for i in range(len(arr))])
        if len(arr) == 0:
            return []
        rank_arr = [(1,arr[0][1])]
        for i in range(1, len(arr)):
            if arr[i][0] != arr[i - 1][0]:
                rank_arr.append((rank_arr[i - 1][0] + 1, arr[i][1]))
            else:
                rank_arr.append((rank_arr[i - 1][0], arr[i][1]))
        
        return [x[0] for x in sorted(rank_arr, key=lambda l: l[1])]
