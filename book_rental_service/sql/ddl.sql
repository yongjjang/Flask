create or replace schema bookrentalservice collate utf8_general_ci;

create or replace table book
(
	id int null,
	ISBN char(40) not null
		primary key,
	Name char(40) null,
	Author char(40) null,
	Price char(20) null,
	Description char(40) null,
	Link char(100) null,
	PicturePath char(100) null,
	canRental tinyint(1) default 1 not null
);

create or replace table user
(
	id int not null
		primary key,
	Name char(20) not null,
	Birthday date not null,
	Gender char(2) null,
	Email char(60) null,
	Telno char(14) null,
	PicturePath char(100) null
);

create or replace table bookrental
(
	ID int not null
		primary key,
	UserId int not null,
	ISBN char(40) not null,
	RentalDate date null,
	ReturnDate date null,
	isRentaled tinyint(1) default 0 null,
	constraint BookRental_book_ISBN_fk
		foreign key (ISBN) references book (ISBN),
	constraint bookrental_user_Name_fk
		foreign key (UserId) references user (id)
);

