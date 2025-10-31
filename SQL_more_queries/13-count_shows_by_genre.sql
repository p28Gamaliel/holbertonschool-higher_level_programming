-- lists all genres
SELECT g.name AS genre, COUNT(tg.tv_show_id) AS number_of_shows
FROM tv_show_genres tg
JOIN genres g ON tg.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;