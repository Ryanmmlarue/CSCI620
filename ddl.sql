create table `buys a`
(
    `User ID`    int         not null,
    `Product ID` varchar(30) not null,
    constraint Product_Buys
        foreign key (`Product ID`) references product (`Product ID`),
    constraint User_Buys
        foreign key (`User ID`) references user (user_id)
);

create table `gives a`
(
    `User ID`   int         not null,
    `Review ID` varchar(30) not null,
    constraint Review_Gives
        foreign key (`Review ID`) references review (`Review ID`),
    constraint User_Gives
        foreign key (`User ID`) references user (user_id)
);

create table `has a`
(
    `Review ID`  varchar(30) not null,
    `Product ID` varchar(30) not null,
    constraint Product_Has
        foreign key (`Product ID`) references product (`Product ID`),
    constraint Review_Has
        foreign key (`Review ID`) references review (`Review ID`)
);

create table product
(
    `Product ID` varchar(30) not null
        primary key,
    Parent       int         null,
    Title        tinytext    null,
    Category     tinytext    null,
    constraint `Product ID`
        unique (`Product ID`)
);

create table user
(
    user_id int not null
        primary key
);




