class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / len(salary[1:-1])