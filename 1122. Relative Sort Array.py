#https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = collections.defaultdict(int)
        result_arr = []
        for el in arr1:
            arr1_dict[el] += 1
        for el in arr2:
            result_arr += [el] * arr1_dict[el]
            arr1_dict.pop(el)
        rest_arr = []
        for el, times in arr1_dict.items():
            rest_arr += [el] * times
        result_arr += sorted(rest_arr)
        return result_arr
        
