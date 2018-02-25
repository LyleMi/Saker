DROP DATABASE IF EXISTS `saker`;

CREATE DATABASE `saker` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `saker`;

CREATE TABLE `project` (
  `pid` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `domain` VARCHAR(100) NULL,
  `desc` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

