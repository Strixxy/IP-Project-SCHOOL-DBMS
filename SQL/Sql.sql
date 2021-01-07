-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.22 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.1.0.6168
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for project
CREATE DATABASE IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;

-- Dumping structure for table project.class_10
CREATE TABLE IF NOT EXISTS `class_10` (
  `STD_ID` int NOT NULL DEFAULT '0',
  `STD_NAME` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_class_10_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.class_10: ~1 rows (approximately)
/*!40000 ALTER TABLE `class_10` DISABLE KEYS */;
INSERT INTO `class_10` (`STD_ID`, `STD_NAME`) VALUES
	(2, 'Jillu');
/*!40000 ALTER TABLE `class_10` ENABLE KEYS */;

-- Dumping structure for table project.class_11
CREATE TABLE IF NOT EXISTS `class_11` (
  `STD_ID` int NOT NULL DEFAULT '0',
  `STD_NAME` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_class_11_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.class_11: ~2 rows (approximately)
/*!40000 ALTER TABLE `class_11` DISABLE KEYS */;
INSERT INTO `class_11` (`STD_ID`, `STD_NAME`) VALUES
	(3, 'Ray'),
	(4, 'Abhi');
/*!40000 ALTER TABLE `class_11` ENABLE KEYS */;

-- Dumping structure for table project.class_12
CREATE TABLE IF NOT EXISTS `class_12` (
  `STD_ID` int NOT NULL DEFAULT '0',
  `STD_NAME` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_class_12_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.class_12: ~3 rows (approximately)
/*!40000 ALTER TABLE `class_12` DISABLE KEYS */;
INSERT INTO `class_12` (`STD_ID`, `STD_NAME`) VALUES
	(1, 'Paul'),
	(5, 'John'),
	(6, 'Akash');
/*!40000 ALTER TABLE `class_12` ENABLE KEYS */;

-- Dumping structure for table project.students
CREATE TABLE IF NOT EXISTS `students` (
  `STD_ID` int NOT NULL AUTO_INCREMENT,
  `STD_NAME` varchar(20) DEFAULT NULL,
  `STD_GRADEE` int DEFAULT NULL,
  `STD_AGE` date DEFAULT NULL,
  `STD_NUMBER` bigint DEFAULT NULL,
  `STD_ADDRESS` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  UNIQUE KEY `STD_ID` (`STD_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.students: ~6 rows (approximately)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`STD_ID`, `STD_NAME`, `STD_GRADEE`, `STD_AGE`, `STD_NUMBER`, `STD_ADDRESS`) VALUES
	(1, 'Paul', 12, '2003-05-13', 8281209675, NULL),
	(2, 'Jillu', 10, '2000-04-23', 8282209678, NULL),
	(3, 'Ray', 11, '2002-05-14', 9246566585, NULL),
	(4, 'Abhi', 11, '2003-12-02', 2255456745, NULL),
	(5, 'John', 12, '2002-06-14', 9567846357, NULL),
	(6, 'Akash', 12, '2003-10-13', 9532560569, NULL);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

-- Dumping structure for table project.teacher
CREATE TABLE IF NOT EXISTS `teacher` (
  `TEACHER_ID` int NOT NULL AUTO_INCREMENT,
  `TEACHER_NAME` varchar(20) DEFAULT NULL,
  `TEACHER_DEPT` varchar(20) DEFAULT NULL,
  `TEACHER_NO` bigint DEFAULT NULL,
  `TEACHER_AGE` date DEFAULT NULL,
  PRIMARY KEY (`TEACHER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.teacher: ~3 rows (approximately)
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` (`TEACHER_ID`, `TEACHER_NAME`, `TEACHER_DEPT`, `TEACHER_NO`, `TEACHER_AGE`) VALUES
	(1, 'Sagar', 'Eco', 9573856473, '2000-04-21'),
	(2, 'Manoj', 'English', 9323920145, '2000-04-23'),
	(3, 'Richie', 'Ip', 9583038950, '1999-10-10');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;

-- Dumping structure for table project.tp1
CREATE TABLE IF NOT EXISTS `tp1` (
  `STD_ID` int NOT NULL AUTO_INCREMENT,
  `STD_NAME` varchar(25) DEFAULT NULL,
  `ENGLISH` int DEFAULT NULL,
  `MALAYALAM` int DEFAULT NULL,
  `MATHS` int DEFAULT NULL,
  `BIOLOGY` int DEFAULT NULL,
  `CHEMISTRY` int DEFAULT NULL,
  `PHYSICS` int DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_tp1_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.tp1: ~3 rows (approximately)
/*!40000 ALTER TABLE `tp1` DISABLE KEYS */;
INSERT INTO `tp1` (`STD_ID`, `STD_NAME`, `ENGLISH`, `MALAYALAM`, `MATHS`, `BIOLOGY`, `CHEMISTRY`, `PHYSICS`) VALUES
	(1, 'Paul', 90, 89, 80, 90, 80, 85),
	(2, 'Abhi', 80, 90, 87, 80, 79, 89),
	(3, 'Joe', 87, 67, 98, 78, 90, 87),
	(6, 'Akash', 76, 89, 84, 76, 98, 6);
/*!40000 ALTER TABLE `tp1` ENABLE KEYS */;

-- Dumping structure for table project.tp2
CREATE TABLE IF NOT EXISTS `tp2` (
  `STD_ID` int NOT NULL AUTO_INCREMENT,
  `STD_NAME` varchar(25) DEFAULT NULL,
  `ENGLISH` int DEFAULT NULL,
  `MALAYALAM` int DEFAULT NULL,
  `MATHS` int DEFAULT NULL,
  `BIOLOGY` int DEFAULT NULL,
  `CHEMISTRY` int DEFAULT NULL,
  `PHYSICS` int DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_tp2_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.tp2: ~2 rows (approximately)
/*!40000 ALTER TABLE `tp2` DISABLE KEYS */;
INSERT INTO `tp2` (`STD_ID`, `STD_NAME`, `ENGLISH`, `MALAYALAM`, `MATHS`, `BIOLOGY`, `CHEMISTRY`, `PHYSICS`) VALUES
	(1, 'Paul', 98, 77, 87, 97, 24, 56),
	(2, 'Abhi', 34, 54, 23, 87, 69, 91);
/*!40000 ALTER TABLE `tp2` ENABLE KEYS */;

-- Dumping structure for table project.tp3
CREATE TABLE IF NOT EXISTS `tp3` (
  `STD_ID` int NOT NULL AUTO_INCREMENT,
  `STD_NAME` varchar(25) DEFAULT NULL,
  `ENGLISH` int DEFAULT NULL,
  `MALAYALAM` int DEFAULT NULL,
  `MATHS` int DEFAULT NULL,
  `BIOLOGY` int DEFAULT NULL,
  `CHEMISTRY` int DEFAULT NULL,
  `PHYSICS` int DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_tp3_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.tp3: ~1 rows (approximately)
/*!40000 ALTER TABLE `tp3` DISABLE KEYS */;
INSERT INTO `tp3` (`STD_ID`, `STD_NAME`, `ENGLISH`, `MALAYALAM`, `MATHS`, `BIOLOGY`, `CHEMISTRY`, `PHYSICS`) VALUES
	(1, 'Paul', 89, 78, 68, 80, 95, 87);
/*!40000 ALTER TABLE `tp3` ENABLE KEYS */;

-- Dumping structure for table project.tp4
CREATE TABLE IF NOT EXISTS `tp4` (
  `STD_ID` int NOT NULL AUTO_INCREMENT,
  `STD_NAME` varchar(25) DEFAULT NULL,
  `ENGLISH` int DEFAULT NULL,
  `MALAYALAM` int DEFAULT NULL,
  `MATHS` int DEFAULT NULL,
  `BIOLOGY` int DEFAULT NULL,
  `CHEMISTRY` int DEFAULT NULL,
  `PHYSICS` int DEFAULT NULL,
  PRIMARY KEY (`STD_ID`),
  CONSTRAINT `FK_tp4_students` FOREIGN KEY (`STD_ID`) REFERENCES `students` (`STD_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table project.tp4: ~0 rows (approximately)
/*!40000 ALTER TABLE `tp4` DISABLE KEYS */;
INSERT INTO `tp4` (`STD_ID`, `STD_NAME`, `ENGLISH`, `MALAYALAM`, `MATHS`, `BIOLOGY`, `CHEMISTRY`, `PHYSICS`) VALUES
	(1, 'Paul', 45, 98, 78, 69, 79, 86);
/*!40000 ALTER TABLE `tp4` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
