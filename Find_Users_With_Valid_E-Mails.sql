select * from Users 
where mail like '[a-Z]%leetcode.com' and
substring(mail, 1, len(mail)-13) not like '%[^0-9a-Z_.-]%';
