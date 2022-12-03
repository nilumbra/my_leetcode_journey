# Write your MySQL query statement below
SELECT E.name AS Employee FROM Employee E, Employee M WHERE E.managerID = M.id AND E.salary > M.salary;