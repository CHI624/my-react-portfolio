Question 1:
select name
from sakila.language
order by name asc;

Question 2:
select first_name, last_name
from sakila.actor
where last_name Like '%SON%'
order by first_name;

Question 3:
select address
from sakila.address
where address2 is not null and address2 <> ' '
order by address2;
Question 4:
SELECT COUNT(DISTINCT film.film_id) AS num_film
FROM sakila.film
JOIN sakila.film_actor ON film.film_id = film_actor.film_id
JOIN sakila.actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Crocodile' OR actor.first_name = 'Shark';
Question 5: 
SELECT last_name
FROM sakila.actor
GROUP BY last_name
HAVING COUNT(*) = 1;
Question 6:
SELECT last_name
FROM sakila.actor
WHERE last_name = 'Thompson';
Question 7:
SELECT COUNT(DISTINCT last_name) AS num_distinct_last_names
FROM sakila.actor;
Question 8:
SELECT AVG(length) AS average_running_time
FROM sakila.film;
Question 9:
SELECT SUM(amount)
FROM sakila.payment;
Question 10:
Select count(customer_id)
From sakila.customer
GROUP BY store_id;
Question 11:
Select staff_id, first_name, last_name, store_id, district
From sakila.address, sakila.staff
Where district = '%Toronto%';
Question 12:
select name
From sakila.language
order by name asc;
Question 13:
select address
from sakila.address
where address2 is not null and address2 != ' ';
Question 14:
SELECT AVG(length) AS average_running_time
FROM sakila.film;
Question 15:
SELECT *
FROM sakila.film
WHERE rental_duration = (
    SELECT MAX(rental_duration)
    FROM sakila.film
    WHERE length >= 180
)
ORDER BY film_id ASC;
Question 16: Error Code: 1140. In aggregated query without GROUP BY, expression #2 of SELECT list contains nonaggregated column 'sakila.film.rental_duration'; this is incompatible with sql_mode=only_full_group_by

SELECT c.customer_id, c.first_name, c.last_name,
       COUNT(r.rental_id) AS renting_times,
       SUM(p.amount) AS total_payment
FROM sakila.customer c
JOIN sakila.rental r ON c.customer_id = r.customer_id
JOIN sakila.payment p ON r.rental_id = p.rental_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING renting_times >= 40
ORDER BY renting_times ASC;







