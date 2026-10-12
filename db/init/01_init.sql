create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

create user if not exists 'eunche'@'localhost' identified by 'q1w2e3';
create user if not exists 'eunche'@'%' identified by 'q1w2e3';

grant select, insert, update, delete on shopping_db.* to 'eunche'@'%';
grant select, insert, update, delete on shopping_db.* to 'eunche'@'localhost';
flush privileges;
