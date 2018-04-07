DROP DATABASE IF EXISTS `saker`;

CREATE DATABASE `saker` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `saker`;

CREATE TABLE `project` (
  `uid` VARCHAR(32) NOT NULL,
  `name` VARCHAR(100) NULL,
  `domain` VARCHAR(100) NULL,
  `desc` VARCHAR(1000) NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `site` (
  `uid` VARCHAR(32) NOT NULL,
  -- project id
  `pid` VARCHAR(32) NOT NULL,
  `domain` VARCHAR(100) NULL,
  `desc` VARCHAR(1000) NULL,
  PRIMARY KEY (`iuidd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE USER 'saker'@'localhost' IDENTIFIED BY 'random_password';
GRANT all privileges ON saker.* TO 'saker'@'localhost';

CREATE USER 'backup'@'localhost' IDENTIFIED BY 'another_random_password';
GRANT SELECT ON saker.* TO 'backup'@'localhost';
