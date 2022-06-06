# Write your MySQL query statement below
# select email 
# from
#     (select email, count(*)
#      from Person
#      group by email
#      having count(*) > 1) e;
 
 select email
 from
(select email, count(email) as q
     from Person
     group by email
     having q > 1) e;