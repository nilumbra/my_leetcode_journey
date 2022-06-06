# Write your MySQL query statement below
select date_format(trans_date, '%Y-%m') month, 
       country, 
       count(state) trans_count,
       count(case when state='approved' then state end) approved_count, 
       sum(amount) trans_total_amount,
       sum(case when state='approved' then amount else 0 end) approved_total_amount
from Transactions t 
group by 1, 2