
# sql=structured query language

# mysql is a relational data base management system (rdbms)
# where in we store data in form of table rows and column

# relational data base management system (rdbms) is based on sql it has mysql microsoft sql server oracle etc


# mysql workbench

# it is ui for mysql for epx graphical tool for working with mysql servers and database
# it easies for creating database table and saving the data

# mysql ye case insensetive hota he

# how mysql works

# in mysql we create data bases and in database we create table


# sql and nosql

# sql follows the rdbms model and nosql follows the json
# mysql suppose sql and mongobd suppose nosql

# attribute
# jo table me property set karte he usko hi attribute bolte he


# mysql -u root -p
# isse mysql start kar sakte he
# show databases;
# isse databases show ho jate he
# create database muneedb2;
# isse database create kar sakte he
# use muneebdb
# isse database use kar sakte he


# create TABLE EMPLOYEE(
#     -> EMPID int,
#     -> FirstName varchar(250),
#     -> LastName varchar(250),
#     -> Empage int,
#     -> EmpZone varchar(250)
#     -> );

# ese table create kar sakte he

# auto_increment
# EmpID int not null auto_increment,


# INSERT INTO `muneebdb3`.`employee` (`EMPID`, `EMPNAME`, `EmployeAge`, `EmployeDept`) VALUES ('2', 'muneeb', '24', 'management');
# is tarike se table me insert kar sakte he


#  DESC EMPLOYEE;
# isse table ke column ke type null key default dekh sakte he

# select * from employee2;
# isse saari column ki values dekh sakte he

# select distinct Empage from EMPLOYEE;
# select different values from table ye same values ko ek baar hi dikhata he


# where clause in mysql ye if else condition ki tarah hota he
# select distinct * from EMPLOYEE where Empage=24;


# operators in where clause

# =,!=,<,>,>=,<=,<>,between,like,in,and,or,not

# in operator
# select * from employee4 where empzone in("south","east");
# select * from employee4 where empzone not in("south","east");

# between operator
# select * from employee4 where age between 24 and 30;


# like operator
# ye regex ki tarah hota he 
# isme 2 wildcards hote he % and _   
# % ye 0,1,or more character ke liye hota he
# _ ye single character ke liye hota he
# select * from employee4 where firstname like ("m%");  iska matlab shuru m hona chahiye
# select * from employee4 where firstname like ("%a%"); iska matlab andar a hona chahiye
# select * from employee4 where empzone like("___t");



# update and set
# update employee4 set firstname="harry",lastname="jack",Empzone="north" where EmpID!=1;

# agar safe update ka error he to ye use karenge
# set SQL_SAFE_UPDATES=0;


# alter command for add column
# alter table  employee2 add column Department varchar(100);

# alter command for delete column
# alter table  employee2 drop column Department;

# alter command for modify column
# alter table employee9 modify column empdept int;

# alter commond for add constraint
# alter table department add constraint fk foreign key(EmpID) references employee(EmpID);



# constraint matlab specifies the rules for data in table matlab column me rule set karna

# not null constraint is use for ensure that column can not have null value


# primary key constraint  is use for uniquely identify the each row in table
# we can set empid, licence no,student roll no as primary key because it is unique and we cannot set null in primary key 
# primary key(empID)



# foreign key constraint
# a foreign key is a field in one table referring to the primary key in another table
# child table (referencing):the table with the foreign key
# parent table (referenced):the table with the primary key
# aur jab foreign key banate he tab vohi primary key use kar sakte he jo parent me ho
# aur primary key ek se zada attribute me nahi rak sakte lekin foreign key ek se zada rakh sakte he
# foreign key basically isliye banate he taki dusre table se refrence le sake jese ek table me logon ka data he aur ham ek aur table banana jisme unka hi data add ho jinse refrence le rahe he 



# create table employee(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# Empzone varchar(250),
# primary key(EmpID)
# ); 
# this is a parent table 



# create table Department(
# DeptID int not null,
# DeptName varchar(200),
# primary key (DeptID),
# EmpID int,
# foreign key(EmpID) references employee(EmpID)
# );
# this is child table


# in the employee table EmpID is a primary key
# in the Department table DeptID is a primary key
# and in the Department table EmpID is a foreign key


# parent table (referenced)
# insert no violation
# delete may cause violation because it intigrate violation for that we use on delete cascade and on delete set null isse refrencing wala bhi delete hojayga
# update may cause violation because it intigrate violation for that we use on update cascade and on update set null isse refrencing wala bhi update hojayga


# child table (referencing)
# insert may cause violation
# delete no violation
# updation may cause violation because if the foreign key is not present in primary key of refrenced table

# intigrity matlab same value for database

# violation matlab kisi rule ko todne ko bolte he


# unique constraint
# we can create many attributes as unique but we cannot create many attributes as primary key
# unique(EmpID)

# default constraint
# default "operations" isse default value set kar sakte he

# check constraint
# isko table create karte time use karte he aur ye condition check karta he
# check(age>20)




# extra information

# scaling
# jab website pe load zada pad jata he tab use scaling karni padti he aur scaling 2 type ki hoti he vertical scaling and horizontal scaling

# vertical scaling 
# vertical scaling usko bolte he jab same server ko badate he


# horizontal scaling
# horizontal scaling usko bolte he jab alag alag server use karte he

















