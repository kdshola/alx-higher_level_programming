-- Creates the table unique_id on your MySQL server with unique id and value 1.

CREATE TABLE
	IF NOT EXISTS `unique_id` (
		`id` INT DEFAULT 1 UNIQUE,
		`name` VARCHAR(256)
		);
