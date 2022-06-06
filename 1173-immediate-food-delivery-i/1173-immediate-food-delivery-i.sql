# Write your MySQL query statement below
# WITH immediate as (SELECT COUNT(delivery_id) imm FROM Delivery WHERE order_date = customer_pref_delivery_date),
#       t as (SELECT COUNT(delivery_id) total FROM Delivery)
    
SELECT ROUND(
       COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN delivery_id END) * 100 /
       COUNT(delivery_id), 2) AS immediate_percentage
FROM Delivery;