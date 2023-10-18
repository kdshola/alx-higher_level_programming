-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT `g`.`name` FROM `tv_genres` AS `g`
	INNER JOIN `tv_show_genres` AS `tvg`
	ON `g`.`id` = `tvg`.`genre_id`
	INNER JOIN `tv_shows` as `ts`
	ON `ts`.`id` = `tvg`.`show_id`
	WHERE `ts`.`title` = "Dexter"
 ORDER  BY `g`.`name`;
