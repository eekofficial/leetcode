#https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        res = []
        first_dict = dict()
        second_dict = dict()
        for i in range(len(list1)):
            first_dict[list1[i]] = i
        for i in range(len(list2)):
            second_dict[list2[i]] = i
        for name, index in first_dict.items():
            if second_dict.get(name) != None and index + second_dict[name] < min_sum:
                res = [name]
                min_sum = index + second_dict[name]
            elif second_dict.get(name) != None and index + second_dict[name] == min_sum:
                res.append(name)
        return res
        
