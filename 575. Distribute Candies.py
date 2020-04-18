#https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        sister_need = len(candies) // 2
        candies_counter = collections.defaultdict(int)
        for candie in candies:
            candies_counter[candie] += 1
        candies = list(candies_counter.values())        
        sister_kinds = 0
        for i in range(len(candies)):
            if sister_need == 0:
                break
            candies[i] -= 1
            sister_kinds += 1
            sister_need -= 1
        return sister_kinds
            
        
        
