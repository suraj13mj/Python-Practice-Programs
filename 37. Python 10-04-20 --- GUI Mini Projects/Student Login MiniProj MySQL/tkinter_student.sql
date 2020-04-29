-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2020 at 01:27 PM
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
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `username` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`username`, `password`) VALUES
('ravindra', '1234'),
('samit', '1234'),
('ishita', '1234'),
('sudarshan', '1234'),
('kiran', '1234'),
('laxman', '1234'),
('jaya', '1234'),
('mamata', '1234'),
('rahul', '1234'),
('sagar', '1234'),
('geeta', '1234'),
('manish', '1234'),
('alok', '1234'),
('praneeth', '1234'),
('yogesh', '1234'),
('zayida', '1234'),
('kalim', '1234'),
('ignatius', '1234'),
('tejus', '1234');

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
('Sagar Pai', 110, 'Bangalore,\nKarnataka', 'KLEIT', 'ECE', 'MALE', 1),
('Geeta Janmane', 111, 'H.no-45,\nThane,\nMaharashtra\n670003', 'RVCE', 'CSE', 'FEMALE', 0),
('Manish Malhotra', 112, 'Avenue Street 121\nNew York\nUSA\n196357', 'IIT-D', 'Aerospace', 'MALE', 0),
('Alok Nath', 113, 'Vilas Nagar,\nPalghar,\nMaharashtra\n680014', 'SDM', 'ECE', 'MALE', 1),
('Praneeth Shenoy', 114, 'Suratkal,\nMangalore,\nKarnataka\n530142', 'MSRIT', 'Civil', 'MALE', 1),
('Yogesh Jain', 115, 'Hubli,\nKarnataka', 'AGMR', 'Telecom', 'MALE', 1),
('Zayida Sheikh', 116, 'Mannat,\nJeddah,\nSaudi Arabia', 'RVCE', 'Mech', 'FEMALE', 0),
('Kalim Khan', 117, 'Powai,\nMumabai\nMaharashtra\n650003', 'PES', 'Civil', 'MALE', 1),
('Ignatius Fernandiz', 118, 'Hubli,\nKarnataka', 'AGMR', 'EEE', 'MALE', 1),
('Tejas Bellad', 119, 'Hubli,\nKarnataka', 'BVB', 'Civil', 'MALE', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
