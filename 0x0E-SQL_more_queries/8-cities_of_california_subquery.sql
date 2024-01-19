-- List All the cities of California in the database hbtn_0d_usa
SELECT `cities`.`id`, `cities`.`name` FROM `hbtn_0d_usa`.`cities` WHERE `cities`.`state_id` = (SELECT id FROM `hbtn_0d_usa`.`states` WHERE `states`.`name` = 'California') ORDER BY `cities`.`id`;
