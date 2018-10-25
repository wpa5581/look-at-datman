create table customer (
  id int primary key,
  income int,
  name varchar(255),
  phone varchar(255),
  gender varchar(16),
  address_street varchar(255),
  address_state varchar(255),
  address_zipcode varchar(255)
)

create table dealer (
  id int primary key,
  name varchar(255),
  phone varchar(255)
)

create table brand (
  name varchar(255) primary key,
  country varchar(255),
  reliability varchar(255)
)

create table sale (
  id int primary key,
  customer int foreign key references customer(id)
)

create table vehicle (
  vin int primary key,
  model varchar(255),
  transmission varchar(255),
  mileage int,
  transmission varchar(255),
  engine varchar(255),
  color varchar(255),
  brand varchar(255) foreign key references brand(name),
  dealer int foreign key references dealer(id),
  sale int foreign key references sale(id),
  customer int foreign key references customer(id)
)

create table brand_dealer (
  brand varchar(255) foreign key references brand(name),
  dealer int foreign key references dealer(id)
)
