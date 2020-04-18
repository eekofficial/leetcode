#https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums) -> int:
        nums_dict = collections.defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        max_degree_num = 0
        max_degree_nums = []
        max_degree = 0
        for num, times in nums_dict.items():
            if times > max_degree:
                max_degree = times
                max_degree_num = num
                max_degree_nums = [num]
            elif times == max_degree and num != max_degree_num:
                max_degree_nums.append(num)
        first_dict = dict()
        last_dict = dict()
        for num in max_degree_nums:
            for i in range(len(nums)):
                if nums[i] == num and first_dict.get(num) == None:
                    first_dict[num] = i
                if nums[i] == num:
                    last_dict[num] = i
        min_subarray = float('inf')
        for num, index in first_dict.items():
            if last_dict[num] - index + 1 < min_subarray:
                min_subarray = last_dict[num] - index + 1
        return min_subarray
