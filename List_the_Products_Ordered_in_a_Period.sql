select b.product_name, sum(a.unit) as unit from Orders as a
inner join Products as b 
on a.product_id = b.product_id
where month(order_date) = 2 and year(order_date) = 2020
group by product_name
having sum(unit) >= 100
