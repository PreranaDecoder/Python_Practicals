create database demo;
use demo;
create user 'prerana'@'localhost'IDENTIFIED BY 'Mumbai#100';
grant all on demo.*to 'prerana'@'localhost';
create table student(PRN varchar(12),First_Name varchar(20),Middle_Name varchar(20),Last_Name varchar(20),Address varchar(30),
Mobile_Number int, Email_ID varchar(20),DOB date);