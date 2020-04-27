-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2020 at 06:28 PM
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
-- Database: `tkinter_student`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `name` varchar(30) NOT NULL,
  `rollno` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `college` varchar(30) NOT NULL,
  `branch` varchar(30) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `news` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `rollno`, `address`, `college`, `branch`, `sex`, `news`) VALUES
('Ravindra Singh', 101, 'Jodhapur,\nRajasthan', 'RVCE', 'Mech', 'MALE', 1),
('Samit Patel', 102, 'Cuttack,\nOdisha', 'SDM', 'ECE', 'MALE', 0),
('Ishita Mehta', 103, 'Indore,\nMadhya Prdesh', 'RVCE', 'CSE', 'FEMALE', 1),
('Sudarshan Nirwani', 104, 'Hubli,\nKarnataka', 'SDM', 'ISE', 'MALE', 0),
('Kiran Devihosur', 105, 'Pune,\nMaharashtra', 'BVB', 'Telecom', 'MALE', 0),
('Laxman Nair', 106, 'Kannur,\nKerala', 'AGMR', 'Aerospace', 'MALE', 1),
('Jaya Reddy', 107, 'Vishakhapatnam,\nAndhra Pradesh', 'IIT-D', 'Civil', 'FEMALE', 0),
('Mamata Vijayan', 108, 'Hyderabad,\nTelengana', 'MSRIT', 'EEE', 'FEMALE', 1),
('Rahul Porwal', 109, 'Ranchi,\nJharkhand', 'PES', 'Robotics', 'MALE', 0),
('Sagar Pai', 110, 'Bangalore,\nKarnataka', 'KLEIT', 'ECE', 'MALE', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
