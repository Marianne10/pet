create database pet;
use pet;
 create table contatos(
    con_id int auto_increment primary key, 
    con_email varchar(255) not null,
    con_assnto varchar(255) not null,
    con_descricao varchar(255) not null
 );
 