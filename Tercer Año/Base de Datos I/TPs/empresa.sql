-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-06-2021 a las 16:06:25
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `depto_no` int(11) NOT NULL,
  `nombre_depto` text NOT NULL,
  `localidad` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`depto_no`, `nombre_depto`, `localidad`) VALUES
(10, 'Desarrollo Software', 'Calamuchita'),
(20, 'Analisis Sistemas', 'Rio Cuarto'),
(30, 'Contabilidad', 'Colon'),
(40, 'Ventas', 'Capital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `edad` int(11) NOT NULL,
  `oficio` varchar(40) NOT NULL,
  `dir` text NOT NULL,
  `fecha_alt` date NOT NULL,
  `salario` int(11) NOT NULL,
  `comision` int(11) NOT NULL,
  `fk_depto_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`codigo`, `nombre`, `edad`, `oficio`, `dir`, `fecha_alt`, `salario`, `comision`, `fk_depto_no`) VALUES
(1, 'Rocha Vargas Hector', 27, 'Vendedor', 'Martinoli', '1983-05-12', 12000, 0, 40),
(2, 'Lopez Hernandes Julio', 27, 'Analista', 'Ricardo Rojas', '1982-07-14', 13000, 1500, 20),
(3, 'Esquivel Jose ', 31, 'Director', 'Martinoli', '1981-06-05', 16700, 1200, 30),
(4, 'Delgado Carmen', 37, 'Vendedor', 'Granaderos', '1983-03-02', 13400, 0, 40),
(5, 'Castillo Montes Luis', 17, 'Vendedor', 'Bulnes', '1982-08-12', 16309, 1000, 40),
(6, 'Esquivel Leonel Alfonso', 26, 'Presidente', 'Vidal', '1981-09-12', 15000, 0, 30),
(7, 'Perez Luis', 32, 'Empleado', 'Cabrera', '1980-03-02', 16890, 0, 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`depto_no`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `fk_depto_no` (`fk_depto_no`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `depto_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`fk_depto_no`) REFERENCES `departamentos` (`depto_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
