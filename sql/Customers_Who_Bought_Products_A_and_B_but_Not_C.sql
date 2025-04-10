# Write your MySQL query statement below
select * from Customers
where customer_id not in 
(select customer_id from Orders where product_name = 'C')
and customer_id in 
(select customer_id from Orders where product_name = 'A')
and customer_id in 
(select customer_id from Orders where product_name = 'B')
