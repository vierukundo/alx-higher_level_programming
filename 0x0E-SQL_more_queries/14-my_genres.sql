-- 14-my_genres.sql
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id =
(
	SELECT tv_shows.id
	FROM tv_shows
	WHERE title = "Dexter"
)
ORDER BY tv_genres.name;
