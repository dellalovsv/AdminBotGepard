create table if not exists `bot_admins` (
    id bigint not null,
    phone varchar(30) not null default '0',
    disable int not null default '0',
    date_add date not null default current_date,
    primary key (id)
);
