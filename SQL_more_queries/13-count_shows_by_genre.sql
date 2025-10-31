--
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;