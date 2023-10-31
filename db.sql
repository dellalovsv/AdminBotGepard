ALTER TABLE `admins` ADD `tid` BIGINT NOT NULL DEFAULT '0' COMMENT 'id пользователя телеграм' AFTER `start_work`;

create table if not exists `bot_dillers` (
    id int not null auto_increment,
    name varchar(30) not null unique,
    phone varchar(25) not null default "0",
    address text not null,
    disable int not null default "0",
    date_add date not null default current_date,
    primary key (id)
);
