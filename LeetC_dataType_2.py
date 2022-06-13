# 1491. Average Salary Excluding the Minimum and Maximum Salary
'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:

    3 <= salary.length <= 100
    1000 <= salary[i] <= 106
    All the integers of salary are unique.

'''

class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(len(salary)-1)
        sum = 0
        for i in salary:
            sum = sum + i
        return sum/len(salary)
    def average2(self, salary: list[int]) -> float:
        salary.sort()
        sum = 0
        for i in range(1, len(salary)-1):
            sum = sum + i
        return float("{0:5f}".format(sum/(len(salary)-2)))
    def average3(self, salary: list[int]) -> float:
        # Establish what. the max and min values are first
        max_entry, min_entry = max(salary), min(salary)
        
        # Remove from list before we count # of items in list
        salary.remove(max_entry)
        salary.remove(min_entry)
        
        # Calculate the average (sum/# of items)
        num_of_entries = len(salary)
        avg_salary = sum(salary) / num_of_entries
        return avg_salary

print(Solution().average3([1000,2000,3000]))
print(Solution().average3([4000,3000,1000,2000]))
