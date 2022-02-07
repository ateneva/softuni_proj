DROP SCHEMA IF EXISTS pet_hotel CASCADE;
--ensure schema can be deleted with all its dependencies

CREATE SCHEMA IF NOT EXISTS pet_hotel;

CREATE TABLE IF NOT EXISTS pet_hotel.hotel
(
  hotel_id    INT PRIMARY KEY,
  hotel_name  VARCHAR(25),
  hotel_stars SMALLINT
);

CREATE TABLE IF NOT EXISTS pet_hotel.pet_owner
(
  owner_id   INT PRIMARY KEY,
  owner_name VARCHAR(15),
  owner_age  SMALLINT
);

CREATE TABLE IF NOT EXISTS pet_hotel.dog_room
(
  room_id         INT PRIMARY KEY,
  dog_id          INT,
  hotel_id        INT,
  register_date   DATE,
  unregister_date DATE
);
--ensure records can be deleted in all tables they reference
ALTER TABLE pet_hotel.dog_room ADD FOREIGN KEY (hotel_id)
REFERENCES pet_hotel.hotel(hotel_id) ON DELETE CASCADE;


DROP TABLE IF EXISTS pet_hotel.dog;
CREATE TABLE IF NOT EXISTS pet_hotel.dog
(
  dog_id   INT PRIMARY KEY REFERENCES pet_hotel.dog_room ON DELETE CASCADE,
  owner_id INT,
  dog_name VARCHAR(15),
  dog_age  SMALLINT
);
--ensure records can be deleted in all tables they reference
ALTER TABLE pet_hotel.dog ADD FOREIGN KEY (owner_id)
REFERENCES pet_hotel.pet_owner(owner_id) ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS pet_hotel.cat_room
(
  room_id         INT PRIMARY KEY,
  cat_id          INT,
  hotel_id        INT,
  register_date   DATE,
  unregister_date DATE
);
--ensure records can be deleted in all tables they reference
ALTER TABLE pet_hotel.cat_room  ADD FOREIGN KEY (hotel_id)
REFERENCES pet_hotel.hotel(hotel_id) ON DELETE CASCADE;


--DROP TABLE IF EXISTS pet_hotel.cat;
CREATE TABLE IF NOT EXISTS pet_hotel.cat
(
  cat_id   INT PRIMARY KEY REFERENCES pet_hotel.cat_room ON DELETE CASCADE,
  owner_id INT,
  cat_name VARCHAR(15),
  cat_age  SMALLINT
);
--ensure records can be deleted in all tables they reference
ALTER TABLE pet_hotel.cat ADD FOREIGN KEY (owner_id)
REFERENCES pet_hotel.pet_owner(owner_id) ON DELETE CASCADE;


---alternative syntax
/*
 CREATE TABLE order_items (
    product_no integer REFERENCES products ON DELETE RESTRICT,
    order_id integer REFERENCES orders ON DELETE CASCADE,
    quantity integer,
    PRIMARY KEY (product_no, order_id)
);
 */
---CASCADE specifies that when a referenced row is deleted,
  ----row(s) referencing it should be automatically deleted as well
  
---https://www.postgresql.org/docs/8.2/ddl-constraints.html



