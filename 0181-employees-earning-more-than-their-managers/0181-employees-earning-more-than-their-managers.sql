# Write your MySQL query statement below
SELECT a.name as Employee
from Employee as a JOIN Employee as b
on a.ManagerId = b.Id and a.Salary > b.Salary;
