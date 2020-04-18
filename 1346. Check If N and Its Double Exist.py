#https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr) -> bool:
        arr = sorted(arr)
        for i in range(len(arr)):
            index = self.binary_search(arr, i)
            if index:
                return index
        return False
            
    
    def binary_search(self, arr, i):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if i != mid and arr[mid] == 2 * arr[i]:
                return True
            elif 2 * arr[i] > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return False
