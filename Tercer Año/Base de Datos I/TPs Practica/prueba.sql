-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-06-2026 a las 02:36:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `nombresyrazas` ()   Select m.nombre, r.raza
from prueba.razas as r, prueba.mascotas as m
where m.idraza = r.idrazas$$

--
-- Funciones
--
CREATE DEFINER=`root`@`localhost` FUNCTION `mayor` (`vraza` VARCHAR(45)) RETURNS INT(11)  BEGIN
declare edad int;
set edad=(select max(m.edad) from prueba.mascotas m,prueba.razas r where m.idraza=r.idrazas and
r.raza=vraza);
RETURN edad;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acciones`
--

CREATE TABLE `acciones` (
  `idacciones` int(11) NOT NULL,
  `accion` varchar(255) NOT NULL,
  `fecha_hora` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `acciones`
--

INSERT INTO `acciones` (`idacciones`, `accion`, `fecha_hora`) VALUES
(1, 'Se inserto marga con Id= 4', '2026-06-07 21:31:15'),
(2, 'Se inserto marga con Id= 5', '2026-06-07 21:32:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascotas`
--

CREATE TABLE `mascotas` (
  `idmascotas` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `idraza` int(11) NOT NULL,
  `edad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mascotas`
--

INSERT INTO `mascotas` (`idmascotas`, `nombre`, `idraza`, `edad`) VALUES
(1, 'hanna', 1, 2),
(2, 'aron', 2, 5),
(3, 'sara', 3, 8),
(4, 'marga', 3, 10);

--
-- Disparadores `mascotas`
--
DELIMITER $$
CREATE TRIGGER `acciones_mascotas` AFTER INSERT ON `mascotas` FOR EACH ROW Insert into acciones(accion) value (concat('Se inserto ', NEW.nombre,' con Id= ', NEW.idmascotas))
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `razas`
--

CREATE TABLE `razas` (
  `idrazas` int(11) NOT NULL,
  `raza` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `razas`
--

INSERT INTO `razas` (`idrazas`, `raza`) VALUES
(1, 'chiguagua'),
(2, 'pincher'),
(3, 'manto negro');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_nombresyrazas`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_nombresyrazas` (
`nombre` varchar(45)
,`raza` varchar(45)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_nombresyrazas`
--
DROP TABLE IF EXISTS `vista_nombresyrazas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_nombresyrazas`  AS SELECT `m`.`nombre` AS `nombre`, `r`.`raza` AS `raza` FROM (`razas` `r` join `mascotas` `m`) WHERE `m`.`idraza` = `r`.`idrazas` ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acciones`
--
ALTER TABLE `acciones`
  ADD PRIMARY KEY (`idacciones`);

--
-- Indices de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD PRIMARY KEY (`idmascotas`),
  ADD KEY `mascotas_ibfk_1` (`idraza`),
  ADD KEY `nombre_i` (`nombre`);

--
-- Indices de la tabla `razas`
--
ALTER TABLE `razas`
  ADD PRIMARY KEY (`idrazas`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acciones`
--
ALTER TABLE `acciones`
  MODIFY `idacciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  MODIFY `idmascotas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `razas`
--
ALTER TABLE `razas`
  MODIFY `idrazas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD CONSTRAINT `mascotas_ibfk_1` FOREIGN KEY (`idraza`) REFERENCES `razas` (`idrazas`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
