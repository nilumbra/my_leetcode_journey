# Write your MySQL query statement below
with cdt as (
select * from Calls 
union all
select to_id, from_id, duration from Calls)

select from_id person1, to_id person2, count(*) call_count, sum(duration) total_duration
from cdt 
where from_id < to_id 
group by 1,2 

#select count(*) call_count from cdt where from_id < to_id group by 1, 2
