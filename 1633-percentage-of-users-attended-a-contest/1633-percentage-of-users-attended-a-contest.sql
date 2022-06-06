# SELECT COUNT(user_id) as reg_users FROM Register GROUP BY contest_id;
# Write your MySQL query statement below

WITH users_count as (SELECT COUNT(user_id) AS total_users FROM Users),
     contest_reg as (SELECT contest_id, COUNT(user_id) as reg_users FROM Register GROUP BY contest_id)

SELECT contest_id, round(reg_users/(SELECT total_users FROM users_count)*100, 2) as percentage
FROM contest_reg
ORDER BY percentage DESC, contest_id ASC
