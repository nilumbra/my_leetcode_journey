# Write your MySQL query statement below

select w.name warehouse_name, sum(w.units * p.Width * p.Length * p.Height) volume
from Warehouse w
join Products p
on p.product_id = w.product_id
group by w.name