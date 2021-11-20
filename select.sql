\c artists_2;

SELECT album_name FROM album
WHERE year = 2018;

SELECT title, duration FROM tracks
ORDER BY duration DESC
limit 1;

SELECT title, duration FROM tracks
WHERE duration >= 3.5
ORDER BY duration DESC;

SELECT title FROM playlist
WHERE (year >= 2018) AND (year <=2020);

SELECT  name FROM artist
WHERE not name like '%% %%';

SELECT title FROM tracks
WHERE name like '%%my%%'
