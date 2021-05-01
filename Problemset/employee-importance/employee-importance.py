
# @Title: 员工的重要性 (Employee Importance)
# @Author: cocofe
# @Date: 2021-05-01 10:11:39
# @Runtime: 164 ms
# @Memory: 16.1 MB

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {employee.id: employee for employee in employees}
        def helper(id):
            employee = mapping[id]
            _sum = employee.importance
            for staff in employee.subordinates:
                _sum += helper(staff)
            return _sum
        return helper(id)
