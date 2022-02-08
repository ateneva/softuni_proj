WITH pet_owner_values AS (
  SELECT
    1       AS owner_id,
    'Peter' AS owner_name,
    26      AS owner_age
  
  UNION ALL
    SELECT
    2        AS owner_id,
    'George' AS owner_name,
    32       AS owner_age
  
  UNION ALL
    SELECT
    3        AS owner_id,
    'Amy'    AS owner_name,
    67       AS owner_age
     )

INSERT INTO pet_hotel.pet_owner(owner_id, owner_name, owner_age)
SELECT
  owner_id,
  owner_name,
  owner_age
FROM pet_owner_values;


WITH dogs_values AS (
  SELECT
    1         AS dog_id,
    1         AS owner_id,
    'Fluffy'  AS dog_name,
    2         AS dog_age
  
  UNION ALL
    SELECT
    2         AS dog_id,
    3         AS owner_id,
    'Bully'   AS dog_name,
    3         AS dog_age
  
  UNION ALL
    SELECT
    3         AS dog_id,
    1         AS owner_id,
    'Rousey'  AS dog_name,
    5         AS dog_age
     )

INSERT INTO pet_hotel.dog(dog_id, owner_id, dog_name, dog_age)
SELECT
   dog_id,
   owner_id,
   dog_name,
   dog_age
FROM dogs_values;

WITH dogs_room_values AS (
  SELECT
    1            AS room_id,
    1            AS dog_id,
    1            AS hotel_id,
    '2020-06-08' :: DATE AS register_date,
    '2020-06-10' :: DATE AS unregister_date
  
  UNION ALL
    SELECT
    2            AS room_id,
    2            AS dog_id,
    2            AS hotel_id,
    '2020-06-10' :: DATE AS register_date,
    '2020-06-15' :: DATE AS unregister_date
  
  UNION ALL
    SELECT
    3            AS room_id,
    3            AS dog_id,
    2            AS hotel_id,
    '2020-06-20' :: DATE AS register_date,
    '2020-06-23' :: DATE AS unregister_date
     )

INSERT INTO pet_hotel.dog_room(
  room_id,
  dog_id,
  hotel_id,
  register_date,
  unregister_date
)
SELECT
  room_id,
  dog_id,
  hotel_id,
  register_date,
  unregister_date
FROM dogs_room_values;


WITH cats_values AS (
  SELECT
    1         AS cat_id,
    2         AS owner_id,
    'Tommy'   AS cat_name,
    1         AS cat_age
  
  UNION ALL
    SELECT
    2         AS cat_id,
    3         AS owner_id,
    'Jessy'   AS cat_name,
    7         AS cat_age
  
  UNION ALL
    SELECT
    3         AS cat_id,
    1         AS owner_id,
    'Bubbles' AS cat_name,
    3         AS cat_age
     )

INSERT INTO pet_hotel.cat(cat_id, owner_id, cat_name, cat_age)
SELECT
   cat_id,
   owner_id,
   cat_name,
   cat_age
FROM cats_values;

WITH cats_room_values AS (
  SELECT
    1            AS room_id,
    1            AS cat_id,
    1            AS hotel_id,
    '2020-06-08' :: DATE AS register_date,
    '2020-06-10' :: DATE AS unregister_date
  
  UNION ALL
    SELECT
    2            AS room_id,
    2            AS cat_id,
    2            AS hotel_id,
    '2020-06-10' :: DATE AS register_date,
    '2020-06-15' :: DATE AS unregister_date
  
  UNION ALL
    SELECT
    3            AS room_id,
    3            AS cat_id,
    2            AS hotel_id,
    '2020-06-20' :: DATE AS register_date,
    '2020-06-23' :: DATE AS unregister_date
     )

INSERT INTO pet_hotel.cat_room(
  room_id,
  cat_id,
  hotel_id,
  register_date,
  unregister_date
)
SELECT
  room_id,
  cat_id,
  hotel_id,
  register_date,
  unregister_date
FROM cats_room_values;


INSERT INTO pet_hotel.hotel(hotel_id, hotel_name, hotel_stars)
VALUES(1, 'Grand Pets Hotel', 5);

INSERT INTO pet_hotel.hotel(hotel_id, hotel_name, hotel_stars)
VALUES(2, 'Pets Heaven', 2);