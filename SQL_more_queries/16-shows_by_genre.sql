-- Lists all shows and their linked genres from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL
SELECT s.title, g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON g.id = sg.genre_id
ORDER BY s.title ASC, g.name ASC;