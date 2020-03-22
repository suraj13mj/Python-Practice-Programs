-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 22, 2020 at 05:38 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stud_db`
--

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`rollno`, `name`, `percentage`) VALUES
(101, 'Ramesh Raikar', 86.5),
(102, 'Avinash Shamsi', 76.87),
(103, 'Rahul Akkalkot', 87.65),
(104, 'Advay Raikar', 98.76),
(105, 'Shreyas Shetty', 73.45),
(106, 'Anusha Anvekar', 87.1),
(107, 'Nehal Rao', 65),
(108, 'Racheal Laxmish', 45.98),
(109, 'Gail Wyanand', 87.98),
(110, 'Howard Roark', 98.45);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
