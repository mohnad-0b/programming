class Solution:
    def average(self, salary: List[int]) -> float:
        salarys = sorted(salary)
        avg =0

        for salary in salarys[1:-1]:
            avg += salary


        return avg/(len(salarys)-2)