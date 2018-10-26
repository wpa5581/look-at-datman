create table if not exists customer (
  id int primary key,
  income int,
  name varchar(255),
  phone varchar(255),
  gender varchar(16),
  address_street varchar(255),
  address_state varchar(255),
  address_zipcode varchar(255)
);

create table if not exists dealer (
  id int primary key,
  name varchar(255),
  phone varchar(255)
);

create table if not exists brand (
  name varchar(255) primary key,
  country varchar(255),
  reliability varchar(255)
);

create table if not exists sale (
  id int primary key,
  customer int references customer(id),
  dealer int references dealer(id)
);

create table if not exists vehicle (
  vin int primary key,
  model varchar(255),
  transmission varchar(255),
  mileage int,
  engine varchar(255),
  color varchar(255),
  brand varchar(255) references brand(name),
  dealer int references dealer(id),
  sale int references sale(id),
  customer int references customer(id)
);

create table if not exists brand_dealer (
  brand varchar(255) references brand(name),
  dealer int references dealer(id)
);
