#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_dict = collections.defaultdict(list)
        p_id = 0
        for p in groupSizes:
            groups_dict[p].append(p_id)
            p_id += 1
        result = []
        for group_size, persons in groups_dict.items():
            i = 0
            while i < len(persons):
                if i % group_size == 0:
                    result.append([])
                result[len(result) - 1].append(persons[i])
                i += 1
        return result
                
