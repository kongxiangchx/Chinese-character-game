create database Chinese;
use Chinese;
create table user(
account varchar(30),
password varchar(30),
nickname varchar(30) unique,
sex varchar(10),
poem_score int,
idiom_score int,
primary key(account)
);
create table sentence(
sen_id int,
sen_up varchar(50),
sen_next varchar(50),
sen_author varchar(15),
sen_name varchar(50),
primary key(sen_id)
);
create table idiom(
idiom_id int,
idiom_text varchar(20),
primary key(idiom_id)
);
load data local infile "d:/python-project/python大作业/数据采集/成语.txt" into table idiom fields terminated by ',' lines terminated by '\r\n';
load data local infile "d:/python-project/python大作业/数据采集/诗词2.txt" into table sentence fields terminated by ',' lines terminated by '\r\n';