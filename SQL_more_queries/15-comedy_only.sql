-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id
JOIN tv_genres AS g ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;