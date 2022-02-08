SELECT *
FROM pet_hotel.dog_room;


SELECT
cat_id
FROM pet_hotel.cat_room
WHERE hotel_id = 2;

SELECT *
FROM pet_hotel.pet_owner
ORDER BY
  owner_age DESC;

SELECT
  COUNT(cat_id)
FROM pet_hotel.cat
WHERE cat_age >=3;

DELETE
FROM pet_hotel.cat
WHERE cat_age <=2;


DELETE
FROM pet_hotel.dog
WHERE dog_age <=2;
