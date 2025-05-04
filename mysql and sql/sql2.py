
# case statement in mysql

# select firstname, lastname, age, case when age>25 then "employee with exprerience.Eligible for Sr.profile"
# when age=25 then "the employee is mid-experienced level.Eligible"
# else "freshers... new to the company"
# end as eligibility     ye temprary column banata he
# from employee;

# aggregate function:-

# sum()
# select sum(age) from employee;
# select sum(age) as sum_of_age from employee; 

# avg()
# select avg(age) as avg_of_age from employee;

# count()
# select count(age) as count from employee where age>=25;

# max()
# select max(age) from employee;

# min()
# select min(age) as smallestage from employee;



# delete table
# drop table department;

# delete
# delete from employee;
# isse saari rows delete ho jati he
# delete from employee where firstname="hamza";
# isse particularly row delete kar sakte he



# order by acending order
# select * from employee order by age;

# order by decending order
# select * from employee order by age desc;


# limit clause 
# select * from employee limit 2;
# isse row ki limit set kar sakte he 



# join
# join mtlab cross product + conditon
# aur join me foreign key ka use zaruri hota he kyuki dusri table se refrencd le rahe he

# table employee
# +-------+-------------+-----------+---------+---------+
# | EmpID | firstname   | lastname  | Empzone | address |
# +-------+-------------+-----------+---------+---------+
# |     1 | muneeb      | ur rehman | north   | bhopal  |
# |     2 | abdul       | rehman    | north   | mumbai  |
# |     3 | abdullah    | ahmend    | south   | delhi   |
# |     4 | abdurrehman | khan      | west    | agra    |
# |     5 | hamza       | ali       | north   | ajmair  |
# |     6 | saad        | khan      | south   | pune    |
# +-------+-------------+-----------+---------+---------+

# table department
# +--------+-------+-----------+
# | Deptno | EmpID | Name      |
# +--------+-------+-----------+
# | D01    |     2 | HR        |
# | D02    |     4 | marketing |
# | D03    |     3 | finance   |
# | D04    |     5 | IT        |
# | D05    |     2 | manager   |
# +--------+-------+-----------+


# cross product
# jab bhi ek table ko dusre table se multiply karte he usi ko cross product
# select * from employee,Department;
# isse employee hi har ek row Department ke saari rows ke saath aaygi

# +-------+-------------+-----------+---------+---------+--------+-------+-----------+
# | EmpID | firstname   | lastname  | Empzone | address | Deptno | EmpID | Name      |
# +-------+-------------+-----------+---------+---------+--------+-------+-----------+
# |     1 | muneeb      | ur rehman | north   | bhopal  | D05    |     2 | manager   |
# |     1 | muneeb      | ur rehman | north   | bhopal  | D04    |     5 | IT        |
# |     1 | muneeb      | ur rehman | north   | bhopal  | D03    |     3 | finance   |
# |     1 | muneeb      | ur rehman | north   | bhopal  | D02    |     4 | marketing |
# |     1 | muneeb      | ur rehman | north   | bhopal  | D01    |     2 | HR        |
# |     2 | abdul       | rehman    | north   | mumbai  | D05    |     2 | manager   |
# |     2 | abdul       | rehman    | north   | mumbai  | D04    |     5 | IT        |
# |     2 | abdul       | rehman    | north   | mumbai  | D03    |     3 | finance   |
# |     2 | abdul       | rehman    | north   | mumbai  | D02    |     4 | marketing |
# |     2 | abdul       | rehman    | north   | mumbai  | D01    |     2 | HR        |
# |     3 | abdullah    | ahmend    | south   | delhi   | D05    |     2 | manager   |
# |     3 | abdullah    | ahmend    | south   | delhi   | D04    |     5 | IT        |
# |     3 | abdullah    | ahmend    | south   | delhi   | D03    |     3 | finance   |
# |     3 | abdullah    | ahmend    | south   | delhi   | D02    |     4 | marketing |
# |     3 | abdullah    | ahmend    | south   | delhi   | D01    |     2 | HR        |
# |     4 | abdurrehman | khan      | west    | agra    | D05    |     2 | manager   |
# |     4 | abdurrehman | khan      | west    | agra    | D04    |     5 | IT        |
# |     4 | abdurrehman | khan      | west    | agra    | D03    |     3 | finance   |
# |     4 | abdurrehman | khan      | west    | agra    | D02    |     4 | marketing |
# |     4 | abdurrehman | khan      | west    | agra    | D01    |     2 | HR        |
# |     5 | hamza       | ali       | north   | ajmair  | D05    |     2 | manager   |
# |     5 | hamza       | ali       | north   | ajmair  | D04    |     5 | IT        |
# |     5 | hamza       | ali       | north   | ajmair  | D03    |     3 | finance   |
# |     5 | hamza       | ali       | north   | ajmair  | D02    |     4 | marketing |
# |     5 | hamza       | ali       | north   | ajmair  | D01    |     2 | HR        |
# |     6 | saad        | khan      | south   | pune    | D05    |     2 | manager   |
# |     6 | saad        | khan      | south   | pune    | D04    |     5 | IT        |
# |     6 | saad        | khan      | south   | pune    | D03    |     3 | finance   |
# |     6 | saad        | khan      | south   | pune    | D02    |     4 | marketing |
# |     6 | saad        | khan      | south   | pune    | D01    |     2 | HR        |
# +-------+-------------+-----------+---------+---------+--------+-------+-----------+




# natural join
# jab bhi common attributes ki value ko equalize karna hoto natural join use karte he

# ques=find the employee name who is working in department

# select * from employee,Department where employee.EmpID=department.EmpID; 
# select * from  employee natural join department;
# isse jo same honge bas vohi ayenge
    

# self join

# table study
# +--------+-------+------+
# | s-id   | c-id  |since | 
# +--------+-------+------+
# | s1    |    c1  | 2016 |
# | s2    |    c2  | 2017 |
# | s3    |    c3  | 2017 |
# | s1    |    c4  | 2017 |
# | s4    |    c5  | 2017 |
# +--------+-------+------+

# isme jo s-id vo foreign key he taki dusri table se refrence le rahi he
# aur jo c-id vo bhi foreign key he taki vo bhi dusri table se refrence le rahi he

# ques=find student id who is enrolled in atleast two courses

# select t1.s_id from study as t1,study as t2 where t1.s_id=t2.s_id and t1.c_id<>t2.c_id;


# equi join

# ques find where employee address same as dept address
# select namee,Empaddress,DeptName from employee2,department where employee2.Empid=department.Empid and employee2.Empaddress=department.location


# left outer join

# select DeptName,location,namee,Empaddress from employee2 left outer join department on (employee2.EmpID=Department.EmpID);
# isse jo condition true he vo to bhejega hi bhejega sath me left wale bhi bhejdega


# right outer join

# select DeptName,location,namee,Empaddress from employee2 right outer join department on (employee2.EmpID=Department.EmpID);
# isse jo condition true he vo to bhejega hi bhejega sath me right wale bhi bhejdega




# group by
# ye attribute ki sare same values ko group me daal deta he aur isme bas vo hi name dikha sakte he jisko check kar rahe he

# write a querry to find the count of total no number employees works in deptname 

# select deptname,count(*) as count from department group by deptname;


# having clause
# ye bas khali group by ke sath kaam karta he kyuki where clause puri table ke liye hota he

# ques= write a name of employee where no of employee less then 2 work in department

# select deptname from department group by deptname having count(*)<2; 

# select namee from employee2,department where employee2.empID=department.EmpID and department.deptname="finance";


# union

# ye column ki value ko combine kar deta he agar value same hoto ek baar hi dikhata he
# aur ye attribute left wali table ke hisab se rakhta he
# no of column must be same in no


