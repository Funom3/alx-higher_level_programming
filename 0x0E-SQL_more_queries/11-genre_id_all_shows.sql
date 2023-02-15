-- Lists all shows contained in the datebase hbtn_0d_tvshows
-- Displays NULL for shows without genres
-- Records are in order of ascending tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
	LEFT JOIN `tv_show_genres` AS g
	ON s.`id` = g.show_id`
  ORDER BY s.`title`, g.`genre_id`;
