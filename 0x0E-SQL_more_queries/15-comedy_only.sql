-- Lists all Comedy shows in the database hbtn_0d_tvshows.

SELECt `ts`.`title`
  FROM `tv_shows` AS `ts`
  	INNER JOIN `tv_show_genres` AS `tsg`
	ON `ts`.`id` = `tvs`.`show_id`

	INNER JOIN `tv_genres` AS `g`
	ON `g`.`id` = `tvs`.`genre_id`
	WHERE `g`.`name` = "Comedy"
 ORDER BY `ts`.`title`;
