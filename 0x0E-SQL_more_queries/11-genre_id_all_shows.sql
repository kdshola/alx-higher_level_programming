-- Lists all shows contained in the database hbtn_0d_tvshows.

SELECT `s`.`title`, `tv_sh`.`genre_id`
  FROM `tv_shows` AS `s`
  	LEFT JOIN `tv_shows_genres` AS `tv_sh`
	ON `s`.`id` = `tv_sh`.`show_id`
  ORDER BY `s`.`title`, `tv_sh`.`genre_d`;
