-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT `s`.`title`, `tv_sh`.`genre_id`
  FROM `tv_shows` AS `s`
  	LEFT JOIN `tv_shows_genres` AS `tv_sh`
	ON `s`.`id` = `tv_sh`.`show_id`
	WHERE `tv_sh`.`genre_id` IS NULL
  ORDER BY `s`.`title`, `tv_sh`.`genre_id`;
