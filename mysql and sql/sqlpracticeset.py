
# create database inventorydb;
# use inventorydb;

# create table inventory(
# item_ID int not null,
# item_name varchar(200),
# item_name varchar(200),
# price int,
# primary key(item_ID)
# );


# select * from inventory;

# desc inventory;

# insert into inventory(item_IDitem_nameitem_name) values(14,"IT sector",6);
 
# update inventory set item_ID=10 where item_ID=6;

# set sql_safe_updates=0; 
 
# alter table inventory drop item_name ;

# alter table inventory add column item_name varchar(200);




# use munebdb4;

# create table employee4(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# Empzone varchar(250),
# primary key(EmpID)
# );

# desc employee4;

# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(1,"Tom","hanks","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(2,"abdurrehman","khan","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(3,"abdullah","ahmed","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(4,"muneeb","ur rehman","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(5,"saad","ali khan","east",7000);

# alter table employee4 add column Empsalary int;

# select * from employee4;

# update employee4 set firstname="abdur",lastname="rehman",Empzone="south" where EmpID=2;
# update employee4 set firstname="muneeb",lastname="ur rehman",Empzone="south" where EmpID=3;
# update employee4 set firstname="saad",lastname="ali khan",Empzone="north" where EmpID=4;
# update employee4 set firstname="abdullah",lastname="ahmed",Empzone="north" where EmpID=5;
# update employee4 set firstname="hamza",lastname="ahmed",Empzone="north" where EmpID=6;


# create table Department(
# DeptID int not null,
# DeptName varchar(200),
# primary key (DeptID),
# EmpID int,
# foreign key(EmpID) references employee4(EmpID) on delete cascade on update cascade
# );

# desc Department;

# select * from Department;

# insert into Department(DeptID,DeptName,EmpID) values(10,"marketing",2);
# insert into Department(DeptID,DeptName,EmpID) values(11,"operations",3);
# insert into Department(DeptID,DeptName,EmpID) values(12,"finance",4);


# update Department set EmpID=5 where EmpID=2;


# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(6,"sahil","ifthekhar","north",7000);


# insert into Department(DeptID,DeptName,EmpID) values(14,"IT sector",6);


# update employee4 set EmpID=10 where EmpID=6;


# alter table Department add constraint foreign key(EmpID) references employee4(EmpID) on update cascade;



# create table employee5(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# unique(EmpID)
# );

# desc employee5;

# create table employee6(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# unique(EmpID),
# unique(firstname)
# );

# desc employee6;


# alter table employee6 add column PID int not null;

# alter table employee6 add constraint foreign key(PID) references employee5(EmpID) on delete cascade on update cascade;

# create table employee9(
# EmpID int not null,
# firstname varchar(200) default "operations",
# lastname varchar(200),
# unique(EmpID),
# unique(firstname)
# );

# desc employee9;
 
# alter table employee9 add column age int;

# alter table employee9 add constraint check(age>20);

# insert into employee9(EmpID,lastname,age) values(1,"rehman",24);

# select * from employee9;

# update employee9 set firstname="muneeb",lastname="ur rehman" where age=24;

# set SQL_SAFE_UPDATES=0;
 


# select * from employee4 where empzone="south" and empsalary=7000;

# select * from employee4 where empzone="south" or empsalary=7000;

# select * from employee4 where not empzone="south";

# select * from employee4 where empzone in("south","east");

# select * from employee4 where firstname like ("%a%");

# select * from employee4 where empzone like("___t");

# alter table employee4 add column age int;

# update employee4 set age=24 where firstname="muneeb";

# set sql_safe_updates=0;

# alter table employee4 modify column age int not null;

# update employee4 set age=24 where firstname="muneeb";
# update employee4 set age=21 where firstname="abdur";
# update employee4 set age=21 where firstname="abdullah";
# update employee4 set age=30 where firstname="Tom";
# update employee4 set age=26 where firstname="saad";
# update employee4 set age=24 where firstname="sahil";


# insert into employee4(EmpID,firstname,lastname,Empzone,empsalary,age) values(14,"hamza","ali","west",7000,20);

# desc employee4;

# select * from employee4 where age between 24 and 30;








# use muneebd2;

# create table employee2(
# EmpID int not null,
# name varchar(200),
# Empzone varchar(250),
# Empaddress varchar(200),
# primary key(EmpID)
# );



# create table Department(
# DeptID int not null,
# DeptName varchar(200),
# primary key (DeptID),
# EmpID int,
# location varchar(200),
# foreign key(EmpID) references employee2(EmpID) on delete cascade on update cascade
# );

# alter table  products add column category varchar(200) ;
# alter table  employee2 add column namee varchar(200);

# drop table department;


# desc Department;

# select * from Department;

# insert into Department(DeptID,DeptName,EmpID,location) values(104,"IT",4,"delhi");
# insert into Department(DeptID,DeptName,EmpID,location) values(105,"IT",5,"bhopal");
# insert into Department(DeptID,DeptName,EmpID,location) values(106,"IT",3,"agra");
# insert into Department(DeptID,DeptName,EmpID,location) values(107,"IT",1,"munbai");
# insert into Department(DeptID,DeptName,EmpID,location) values(108,"IT",6,"bhopal");

# update Department set DeptName="marketing" where EmpID=3;
# update Department set DeptName="marketing" where EmpID=1;
# update Department set DeptName="finance" where EmpID=6;

# set SQL_SAFE_UPDATES=0;

# select * from employee2;

# insert into employee2(EmpID,namee,Empzone,Empaddress) values(1,"muneeb","north","bhopal");
# insert into employee2(EmpID,namee,Empzone,Empaddress) values(2,"rehman","north","delhi");
# insert into employee2(EmpID,namee,Empzone,Empaddress) values(3,"abdul","west","mumbai");
# insert into employee2(EmpID,namee,Empzone,Empaddress) values(4,"hamza","east","pune");
# insert into employee2(EmpID,namee,Empzone,Empaddress) values(5,"saad","south","agra");
# insert into employee2(EmpID,namee,Empzone,Empaddress) values(6,"ali","khan","bhopal");

# -- left outer join


# select DeptName,location,namee,Empaddress from department left outer join employee2 on (employee2.EmpID=Department.EmpID);

# -- right outer join

# select DeptName,location,namee,Empaddress from department right outer join employee2 on (employee2.EmpID=Department.EmpID);


# -- equi join

# select namee,Empaddress,DeptName from employee2,department where employee2.Empid=department.Empid and employee2.Empaddress=department.location;

# -- group by

# # write a querry to find the count of total no number employees works in deptname 

# select deptname,count(*) as count from department group by deptname;
 
 
# -- having clause

# # ques write a name of employee where no of employee less then 2 work in department

# select deptname from department group by deptname having count(*)<2; 

# select namee from employee2,department where employee2.empID=department.EmpID and department.deptname="finance";



# -- ------------------------------------- practice ques -----------------------------------

# create table products(
# product_ID int not null,
# product_name varchar(250),
# category varchar(200),
# category varchar(200),
# primary key (product_ID)
# );

# insert into products(product_ID,product_name,category,stock_quantity) values(24,"soap","kichen",50);
# insert into products(product_ID,product_name,category,stock_quantity) values(25,"biscuit","kichen",100);
# insert into products(product_ID,product_name,category,stock_quantity) values(26,"chairs","large_appliance",50);
# insert into products(product_ID,product_name,category,stock_quantity) values(27,"computer","electronics",20);
# insert into products(product_ID,product_name,category,stock_quantity) values(28,"led","electrical",40);
# insert into products(product_ID,product_name,category,stock_quantity) values(29,"phone","electronics",100);

# delete from products;

# create table orders(
# order_ID int not null,
# product_ID int,
# foreign key(product_ID) references products(product_ID)
# );

# alter table products add column stock_quantity int;

# insert into orders(order_ID,product_ID,quantity_ordered) values(104,28,10);
# insert into orders(order_ID,product_ID,quantity_ordered) values(146,25,80);
# insert into orders(order_ID,product_ID,quantity_ordered) values(284,26,8);
# insert into orders(order_ID,product_ID,quantity_ordered) values(105,28,2);

# update products set stock_quantity=70 where product_ID=26;



# set SQL_SAFE_UPDATES=0;


# insert into employee2(EmpID,namee,Empzone,Empaddress) values(1,"muneeb","north","bhopal");

# select * from products;

# select * from orders;

# -- ques list all product that belong to the electronics category

# select * from products where category="electronics";


# -- find product with the hightest quantity

# select max(stock_quantity) from products;

# -- find how many product are in stock for each cetogary

# select product_name,stock_quantity from products where stock_quantity>0;

# -- list of all products that have been ordered atlest onces

# select product_name from products,orders where products.product_ID=orders.product_ID;


# -- find the total number of orders for each product

# select product_name,quantity_ordered from products left outer join orders on products.product_ID=orders.product_ID;

























