CREATE DATABASE DB_parking_config;
USE DB_parking_config;

GRANT SELECT, INSERT, UPDATE, DELETE ON DB_parking_config.* TO 'lk'@'localhost' IDENTIFIED by 'liukai';

CREATE TABLE tbl_settings(
	`id` varchar(50) NOT NULL,
	`parkCode` VARCHAR(200) NOT NULL,
	`billHttpUrl` VARCHAR(200) NOT NULL,
	`carHttpUrl` VARCHAR(200) NOT NULL,
	`img_1_url` VARCHAR(200) NOT NULL,
	`img_2_url` VARCHAR(200) NOT NULL,
	`img_3_url` VARCHAR(200) NOT NULL,
	`invoiceSite` VARCHAR(100) NOT NULL,
	`payStatusHttpUrl` VARCHAR(200) NOT NULL,
	`qcode` VARCHAR(50) NOT NULL,
	`qrcodeHttpUrl` VARCHAR(200) NOT NULL, 
	`tcmName` VARCHAR(50) NOT NULL,
	`tmpCarPlate` VARCHAR(200) NOT NULL,
	unique key `idx_parkCode` (`parkCode`),
	PRIMARY KEY (`id`)
) ENGINE=innodb DEFAULT charset=utf8;
