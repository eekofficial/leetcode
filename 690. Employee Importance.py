#https://leetcode.com/problems/employee-importance/

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates_queue = collections.deque()
        value = 0
        subordinates_queue.append(self.find_employee(employees, id))
        while len(subordinates_queue) != 0:
            e = employees[subordinates_queue.popleft()]
            value += e.importance
            for c in e.subordinates:
                subordinates_queue.append(self.find_employee(employees, c))
        return value
    
    def find_employee(self, employees, id):
        for i in range(len(employees)):
            if employees[i].id == id:
                id_i = i
                break
        return id_i
                
