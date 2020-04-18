#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_el:
                tmp = max_el
                max_el = arr[i]
                arr[i] = tmp
            else:
                arr[i] = max_el
        arr[-1] = -1
        return arr
