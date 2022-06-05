# Write your MySQL query statement below

with 
    a as (select * from Sales where fruit = 'apples'),
    o as (select * from Sales where fruit = 'oranges')
select a.sale_date, sum(a.sold_num - o.sold_num) diff
from a join o
on a.sale_date = o.sale_date
group by 1;