select distinct a.product_id, b.product_name from Sales a
inner join Product b
on a.product_id = b.product_id 
where sale_date >= '2019-01-01' and sale_date<= '2019-03-31' and a.product_id not in 
(
    select product_id from Sales 
where sale_date < '2019-01-01' or sale_date >'2019-03-31'
)
