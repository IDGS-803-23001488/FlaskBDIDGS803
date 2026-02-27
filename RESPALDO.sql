/*
MySQL Backup
Database: bdigs803
Backup Time: 2026-02-26 20:42:04
*/

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `bdigs803`.`alembic_version`;
DROP TABLE IF EXISTS `bdigs803`.`alumnos`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `alumnos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `creates_date` datetime DEFAULT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
BEGIN;
LOCK TABLES `bdigs803`.`alembic_version` WRITE;
DELETE FROM `bdigs803`.`alembic_version`;
INSERT INTO `bdigs803`.`alembic_version` (`version_num`) VALUES ('a4cc52fd4c4e')
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `bdigs803`.`alumnos` WRITE;
DELETE FROM `bdigs803`.`alumnos`;
INSERT INTO `bdigs803`.`alumnos` (`id`,`nombre`,`email`,`creates_date`,`apellidos`,`telefono`) VALUES (1, 'JOSE ANGEL', 'angelgutierrez@gmail.com', '2026-02-16 20:53:31', 'CUELLAR GUTIERREZ', '4776729792'),(2, 'REY ADONAI', 'angelgutierrez@gmail.com', '2026-02-16 20:53:31', 'CUELLAR GUTIERREZ', '4776729792'),(3, 'JUAN CARLO', 'angelgutierrez@gmail.com', '2026-02-16 20:53:31', 'CUELLAR GUTIERREZ', '4776729792'),(6, 'JUANITA', 'angelgutierrez@gmail.com', '2026-02-26 20:41:38', 'LA GUERFANITA', '00000'),(7, 'JUAN PABLO', 'bear.oso2001@gmail.com', '2026-02-26 20:41:55', 'BENEDICTO XX', '00')
;
UNLOCK TABLES;
COMMIT;
