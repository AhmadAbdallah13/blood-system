-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: blood_system
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_citizen`
--

DROP TABLE IF EXISTS `accounts_citizen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_citizen` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `city` varchar(10) NOT NULL,
  `address` varchar(20) NOT NULL,
  `blood_units` int unsigned NOT NULL DEFAULT '0',
  `national_id` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone_number` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number` (`phone_number`),
  CONSTRAINT `accounts_citizen_chk_1` CHECK ((`blood_units` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_citizen`
--

LOCK TABLES `accounts_citizen` WRITE;
/*!40000 ALTER TABLE `accounts_citizen` DISABLE KEYS */;
INSERT INTO `accounts_citizen` VALUES (7,'iyad','shafie','B+','Aqaba','Downtown Aqaba',0,'2288777111','iyad@gmail.com','pbkdf2_sha256$870000$2ZuXZet5mbBM4PnB46jPoa$hmKFrXrLUvFnNlJlLzuk9W7OL9vgKKfoL00q3gL6jCg=','079600221'),(8,'ehab','amawi','AB-','Amman','Khalda',0,'11992288','ehab@gmail.com','pbkdf2_sha256$870000$qAKZmKrZu6iTpodPo2BWfg$1RM8qHDVlIhgqXj5yvbP2KJIp4J/S8kL8wasCeqwAFE=','07940010020'),(9,'ahmad ','abdallah','B+','Amman','Khalda',0,'123456789','ahmad@gmail.com','pbkdf2_sha256$870000$i6m7UOEOpQnywDEv1WnUix$MOyQVNi12HJ7sTrQtFiNuZ3pABI/UsdeHzwslhtM6zk=','079603020'),(10,'hamzeh','mshari','B+','Amman','Khalda',0,'334455667','hamzeh@gmail.com','pbkdf2_sha256$870000$OESnWF5Og0fmBvrVO9KsKC$Q2o0wd+/NE5yHPjFbAAu2svbzG7qc/JxQW5VqN7U8so=','076804030'),(11,'saed','afouri','B+','Irbid','Downtown Irbid',0,'11223344','omar@gmail.com','pbkdf2_sha256$870000$F4Oj73lG9azrUZqvUMbqM0$bH9+BHw+s24EE46EfXxZ2UErAhToLFtbwbNFN8z7AmE=','0794005002'),(12,'azeez','sitech','B+','Amman','Khalda',0,'99887766','azeez@gmail.com','pbkdf2_sha256$870000$YTSy57MuCHknV7cPUFg9pX$IGn0sAE/Ua6vXoAQrqpClMoCtFDTs/7thY3x0OsBLKY=','0798865644'),(13,'mohammed','hijjawi','A+','Amman','Khalda',0,'20012003','mohammed@gmail.com','pbkdf2_sha256$870000$C9hLKuzfk5DmQFJjKGTNEK$gFYFAyODVv6304tW6M9HYEqmedHfK2horI/VB92rBt0=','0792672001'),(14,'mohammed','shraim','A+','Amman','Khalda',0,'2001022320','shraim@gmail.com','pbkdf2_sha256$870000$Q3YdeZk9kW7qAKrBsubuso$3wAFdS+QUoSGW7QhSPqn4noYFD/mm5xXK/0UZst3lKU=','0799476962'),(15,'aseel','bishawi','B+','Amman','Khalda',0,'34534534','aseel@gmail.com','pbkdf2_sha256$870000$7Uez5uC6d437c2hQea44TG$eeLkqWSSh46W9AltWRGPTt8kMd8eAb7VO+R4B9WVdVQ=','07980405021'),(16,'rashid','nabulsi','A+','Irbid','West',0,'19785231','rashid@gmail.com','pbkdf2_sha256$870000$B6IEPF85mrXZ9JqXVks3lM$tiOQUsrpvDuxFq62P0GT8QvFZkag6Ey37+fWmBXbxUA=','05993366210'),(17,'rand','azzam','A+','Amman','Khalda',0,'5252252','rand@gmail.com','pbkdf2_sha256$870000$95ppuugGZfbO631YNmllQp$HQopFkhCVSHO+M8tJMRUFcoLxtJ2J/6vWco+29AsK2c=','079504126'),(18,'ramzi','shaka','A+','Amman','Shmesani',0,'4356345643543','ramzi@gmail.com','pbkdf2_sha256$870000$3ou8ZnGI5NdGJnZMagtWi7$Y9+F0Z8zgh48pmBVO+XiG3dyyu1gqskoBjrmQDCSQmA=','0795067047');
/*!40000 ALTER TABLE `accounts_citizen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_institute`
--

DROP TABLE IF EXISTS `accounts_institute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_institute` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `institute_type` varchar(50) NOT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `city` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `accounts_institute_phone_number_84e3f15f_uniq` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_institute`
--

LOCK TABLES `accounts_institute` WRITE;
/*!40000 ALTER TABLE `accounts_institute` DISABLE KEYS */;
INSERT INTO `accounts_institute` VALUES (1,'Health Institute','Hospital','987654321','hospital@example.com','Los Angeles','456 Avenue','pbkdf2_sha256$870000$zRHaTRJehOiymc5fatTyhO$f2rKRVQnDyZaqSRuZsn7FqKVv88m3Ne4OLZ1q8svspA='),(2,'shmesani hospital','hospital','0795556664','shmesani@gmail.com','amman','amman','pbkdf2_sha256$870000$aasCldVJLS7cWQrlUxgzIY$mSP2HLhq6pZnLRNZaLBfTbqfHLhHQpQvh+VRB89m084='),(3,'zarqa hospital','hospital','07933224477','zarqa@gmail.com','zarqa','tahen','pbkdf2_sha256$870000$8ysWPBXBW9qlLEy7LhLial$cUA0hiV4C125kFCBku6e7Sp/xQz/3dw66wGhP9Ne7OY='),(4,'irbid hospital','hospital','0796003002','irbidhospital@gmail.com','Irbid','Downtown Irbid','pbkdf2_sha256$870000$XrkXzYPc5hZTneqO5gtsVi$LyprjmHatsnbUlEWXJSNQ1jINvB1BCI8YrUHsgulwHw='),(5,'esteshari','hospital','0754123647','esteshari@gmail.com','Amman','wadi saqra','pbkdf2_sha256$870000$FcyK8xtW1QScSXsuUcEapQ$aWgTxXGEitzx1keAivyvCTCsIAsRVKeaj3/X6gkMFSM=');
/*!40000 ALTER TABLE `accounts_institute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add citizen',7,'add_citizen'),(26,'Can change citizen',7,'change_citizen'),(27,'Can delete citizen',7,'delete_citizen'),(28,'Can view citizen',7,'view_citizen'),(29,'Can add institute',8,'add_institute'),(30,'Can change institute',8,'change_institute'),(31,'Can delete institute',8,'delete_institute'),(32,'Can view institute',8,'view_institute'),(33,'Can add khalda hospital appointment',9,'add_khaldahospitalappointment'),(34,'Can change khalda hospital appointment',9,'change_khaldahospitalappointment'),(35,'Can delete khalda hospital appointment',9,'delete_khaldahospitalappointment'),(36,'Can view khalda hospital appointment',9,'view_khaldahospitalappointment'),(37,'Can add urgent case list',10,'add_urgentcaselist'),(38,'Can change urgent case list',10,'change_urgentcaselist'),(39,'Can delete urgent case list',10,'delete_urgentcaselist'),(40,'Can view urgent case list',10,'view_urgentcaselist'),(41,'Can add blood donation appointment',11,'add_blooddonationappointment'),(42,'Can change blood donation appointment',11,'change_blooddonationappointment'),(43,'Can delete blood donation appointment',11,'delete_blooddonationappointment'),(44,'Can view blood donation appointment',11,'view_blooddonationappointment'),(45,'Can add urgent case list',12,'add_urgentcaselist'),(46,'Can change urgent case list',12,'change_urgentcaselist'),(47,'Can delete urgent case list',12,'delete_urgentcaselist'),(48,'Can view urgent case list',12,'view_urgentcaselist');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citizen_dashboard_blooddonationappointment`
--

DROP TABLE IF EXISTS `citizen_dashboard_blooddonationappointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citizen_dashboard_blooddonationappointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `city` varchar(100) NOT NULL,
  `hospital` varchar(200) NOT NULL,
  `citizen_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `chronic_disease` varchar(50) NOT NULL,
  `donated_last_two_months` tinyint(1) NOT NULL,
  `donation_units` varchar(1) DEFAULT NULL,
  `appointment_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citizen_dashboard_blooddonationappointment`
--

LOCK TABLES `citizen_dashboard_blooddonationappointment` WRITE;
/*!40000 ALTER TABLE `citizen_dashboard_blooddonationappointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `citizen_dashboard_blooddonationappointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citizen_dashboard_khaldahospitalappointment`
--

DROP TABLE IF EXISTS `citizen_dashboard_khaldahospitalappointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citizen_dashboard_khaldahospitalappointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `city` varchar(50) NOT NULL,
  `hospital` varchar(100) NOT NULL,
  `citizen_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `appointment_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citizen_dashboard_khaldahospitalappointment`
--

LOCK TABLES `citizen_dashboard_khaldahospitalappointment` WRITE;
/*!40000 ALTER TABLE `citizen_dashboard_khaldahospitalappointment` DISABLE KEYS */;
INSERT INTO `citizen_dashboard_khaldahospitalappointment` VALUES (1,'Amman','Khalda Hospital','kareem hijjawi','kareemhijjawi5@gmail.com','2025-02-22'),(2,'Amman','Khalda Hospital','omar afouri','afouri@gmail.com','2025-05-01'),(3,'Amman','Khalda Hospital','azeez sitech','azeez@gmail.com','2025-02-20'),(4,'Amman','Khalda Hospital','mohammed hijjawi','mohammed@gmail.com','2025-02-28'),(5,'Amman','Khalda Hospital','amr musleh','amr@gmail.com','2025-06-01'),(6,'Amman','Khalda Hospital','amr musleh','amr@gmail.com','2025-06-01'),(7,'Amman','Khalda Hospital','omar hijjawi','omar@gmail.com','2025-03-01'),(8,'Amman','Khalda Hospital','mohammed shraim ','shraim@gmail.com','2025-02-05'),(9,'Amman','Khalda Hospital','mohammed shraim','shraim@gmail.com','2025-03-01'),(10,'Amman','Khalda Hospital','aseel bishawi','aseel@gmail.com','2025-05-01'),(11,'Amman','Khalda Hospital','kareem hijjawi','kareemhijjawi5@gmail.com','2025-02-25'),(12,'Amman','Khalda Hospital','kareem hijjawi','kareemhijjawi5@gmail.com','2025-03-20'),(13,'Amman','Khalda Hospital','salem ammari','salem@gmail.com','2025-06-03'),(14,'Amman','Khalda Hospital','kareem hijjawi','kareemhijjawi5@gmail.com','2025-02-02'),(15,'Amman','Khalda Hospital','rand azzam','rand@gmail.com','2025-05-05'),(16,'Amman','Khalda Hospital','omar alafouri','omar@gmail.com','2025-03-26'),(17,'Amman','Khalda Hospital','omar alafouri','omar@gmail.com','2025-03-26'),(18,'Amman','Khalda Hospital','omar alafouri','omar@gmail.com','2025-03-26');
/*!40000 ALTER TABLE `citizen_dashboard_khaldahospitalappointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'accounts','citizen'),(8,'accounts','institute'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(11,'citizen_dashboard','blooddonationappointment'),(9,'citizen_dashboard','khaldahospitalappointment'),(12,'citizen_dashboard','urgentcaselist'),(5,'contenttypes','contenttype'),(10,'institute_dashboard','urgentcaselist'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2025-02-07 19:28:57.563986'),(2,'contenttypes','0001_initial','2025-02-07 19:28:57.613207'),(3,'auth','0001_initial','2025-02-07 19:28:58.184997'),(4,'admin','0001_initial','2025-02-07 19:28:58.304516'),(5,'admin','0002_logentry_remove_auto_add','2025-02-07 19:28:58.312691'),(6,'admin','0003_logentry_add_action_flag_choices','2025-02-07 19:28:58.318582'),(7,'contenttypes','0002_remove_content_type_name','2025-02-07 19:28:58.406500'),(8,'auth','0002_alter_permission_name_max_length','2025-02-07 19:28:58.458315'),(9,'auth','0003_alter_user_email_max_length','2025-02-07 19:28:58.475821'),(10,'auth','0004_alter_user_username_opts','2025-02-07 19:28:58.481934'),(11,'auth','0005_alter_user_last_login_null','2025-02-07 19:28:58.528745'),(12,'auth','0006_require_contenttypes_0002','2025-02-07 19:28:58.531915'),(13,'auth','0007_alter_validators_add_error_messages','2025-02-07 19:28:58.537633'),(14,'auth','0008_alter_user_username_max_length','2025-02-07 19:28:58.593601'),(15,'auth','0009_alter_user_last_name_max_length','2025-02-07 19:28:58.657917'),(16,'auth','0010_alter_group_name_max_length','2025-02-07 19:28:58.672434'),(17,'auth','0011_update_proxy_permissions','2025-02-07 19:28:58.680323'),(18,'auth','0012_alter_user_first_name_max_length','2025-02-07 19:28:58.738359'),(19,'sessions','0001_initial','2025-02-07 19:28:58.773801'),(20,'accounts','0002_citizen_password_institute_password','2025-02-08 15:07:38.935890'),(21,'accounts','0003_alter_citizen_password_alter_institute_password','2025-02-08 15:25:28.306685'),(22,'accounts','0004_alter_citizen_password_alter_institute_password','2025-02-08 15:54:16.220140'),(23,'accounts','0005_alter_citizen_password_alter_institute_password','2025-02-08 17:04:35.227888'),(24,'accounts','0006_remove_citizen_email_remove_citizen_last_name_and_more','2025-02-10 18:22:22.265564'),(25,'accounts','0006_citizen_phone_number_alter_institute_phone_number','2025-02-11 14:53:19.770155'),(26,'accounts','0007_alter_citizen_address_alter_citizen_blood_type_and_more','2025-02-11 17:37:17.922395'),(27,'accounts','0008_alter_citizen_phone_number','2025-02-11 17:37:17.958545'),(28,'accounts','0009_alter_citizen_phone_number','2025-02-11 17:37:17.997238'),(29,'citizen_dashboard','0001_initial','2025-02-13 17:16:56.184678'),(30,'institute_dashboard','0001_initial','2025-02-15 16:16:08.898186'),(31,'citizen_dashboard','0002_blooddonationappointment','2025-02-17 16:24:50.254148'),(32,'citizen_dashboard','0003_hospital_alter_blooddonationappointment_hospital','2025-02-17 16:24:51.231770'),(33,'citizen_dashboard','0004_alter_blooddonationappointment_hospital_and_more','2025-02-17 16:24:52.034497'),(34,'citizen_dashboard','0005_urgentcaselist','2025-02-17 18:01:17.292806'),(35,'citizen_dashboard','0006_delete_urgentcaselist','2025-02-19 14:44:27.373410');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('f5bkvdxkxoldk8qngzhmu4943nyt3g4l','.eJxVjEsKg0AQBa8ivZaABDezyk2kNa0-mBk_3SGgeHc_KCbLqoKaCVEN9jEp8Cb3TH-EBIYnRxOPA7-anR5VFyilyEGukLSd9jD2m69gmCQeqyy_-Tqxivi_U41RrTh_R96k59uV0Ja_oGUFWI477A:1tlshE:4WnAqOFbwYXY0JRwC6QaIXvNNc0Sq8_tAlePArZcDCo','2025-03-08 16:49:44.024109');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute_dashboard_urgentcaselist`
--

DROP TABLE IF EXISTS `institute_dashboard_urgentcaselist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institute_dashboard_urgentcaselist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_case` varchar(200) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `city` varchar(10) NOT NULL,
  `address` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute_dashboard_urgentcaselist`
--

LOCK TABLES `institute_dashboard_urgentcaselist` WRITE;
/*!40000 ALTER TABLE `institute_dashboard_urgentcaselist` DISABLE KEYS */;
INSERT INTO `institute_dashboard_urgentcaselist` VALUES (1,'surgery','kareem','hijjawi','A+','Amman','Shmesani'),(2,'accedant','khalid','www','AB+','Amman','Shmesani'),(3,'fall down from bridge','ramzi','salameh','O-','Aqaba','Beach Street'),(4,'hand cut','samer','anabousi','B-','Irbid','East'),(5,'leg cut','abd','sarhan','B-','Amman','Shmesani'),(6,'got shot','samer','jaber','AB+','Irbid','Downtown Irbid'),(7,'construction work','murad','majdi','O-','Aqaba','Beach Street'),(8,'animal attack','raed','abadi','B-','Irbid','East'),(9,'surgery ','samiha','majdalawi','O+','Amman','Khalda');
/*!40000 ALTER TABLE `institute_dashboard_urgentcaselist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-23 14:18:34
