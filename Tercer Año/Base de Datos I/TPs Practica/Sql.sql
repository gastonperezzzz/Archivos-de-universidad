-- 1
select empleados.nombre from empleados order by nombre desc;
-- 2
select empleados.nombre,departamentos.localidad from empleados,departamentos where empleados.fk_depto_no=departamentos.depto_no and empleados.oficio like 'Vendedor';
-- 3
select empleados.nombre from empleados where empleados.nombre like '%o';
-- 4
select empleados.nombre, empleados.oficio,empleados.salario from empleados where empleados.dir like 'martinoli';
-- 5
select empleados.nombre,empleados.salario,departamentos.localidad from empleados,departamentos where empleados.fk_depto_no = departamentos.depto_no and empleados.salario>10000 and empleados.salario<13000;
-- 6
Select departamentos.nombre_depto from empleados,departamentos where empleados.fk_depto_no = departamentos.depto_no group by empleados.fk_depto_no having count(empleados.fk_depto_no)>5;
-- 7
Select empleados.nombre, empleados.salario, departamentos.nombre_depto from empleados,departamentos where empleados.fk_depto_no = departamentos.depto_no and oficio=(select oficio from empleados where nombre='Esquivel Leonel Alfonso');
-- 8
Select empleados.nombre,empleados.salario,departamentos.nombre_depto from empleados,departamentos where empleados.fk_depto_no = departamentos.depto_no and empleados.oficio=(select empleados.oficio from empleados where empleados.nombre like 'Castillo Montes Luis') and empleados.comision =0;
-- 9
select empleados.codigo,empleados.nombre,empleados.edad,empleados.oficio,empleados.dir,empleados.fecha_alt,empleados.salario,empleados.comision,empleados.fk_depto_no from empleados,departamentos where empleados.fk_depto_no=departamentos.depto_no and departamentos.nombre_depto like 'Contabilidad' order by empleados.nombre asc;
-- 10
select  empleados.nombre from empleados where  empleados.dir ='Leon' and empleados.oficio like 'Analista' or 'Empleado';
-- 1
insert into empleados values(8,'Perez Luis Carlos','32','Analista','Matagalpa','2001-06-22','15600','0','20'); 
-- 2
insert into departamentos values ('50','General','Cosquin');
-- 3
insert into departamentos values ('60','Pruebas',null);
-- 4
Create table `prueba` (
  `codigo` int(11) not null,
  `nombre` varchar(45) not null,
  `edad` int(11) not null,
  `oficio` varchar(40) not null,
  `dir` text not null,
  `fecha_alt` date not null,
  `salario` int(11) not null,
  `comision` int(11) not null,
  `fk_depto_no` int(11) not null) ;
Insert into prueba select * from empleados where empleados.fk_depto_no=30;
-- 5
create table `prueba2` (
  `cod_depto` text not null,
  `nombre` text not null,
  `salario` int(11) not null
);
insert into prueba2 select empleados.fk_depto_no, empleados.nombre, empleados.salario from empleados where empleados.fk_depto_no=20;
-- 6
update empleados set empleados.salario =empleados.salario*2 where empleados.fk_depto_no=30;
select empleados.nombre,empleados.salario as salario_duplicado from empleados where empleados.fk_depto_no =30;
-- 7
update empleados set empleados.fk_depto_no=20 where empleados.fk_depto_no=30;
select empleados.nombre, empleados.fk_depto_no from empleados where empleados.fk_depto_no =20;
-- 8
update empleados set empleados.salario=empleados.salario*(1.1) where empleados.fk_depto_no=10;
select empleados.nombre, empleados.salario from empleados where empleados.fk_depto_no =10;
-- 9
update departamentos set departamentos.localidad='Zaragoza' where departamentos.depto_no=10;
select departamentos.depto_no, departamentos.localidad from departamentos where departamentos.depto_no=10;
-- 10
update prueba set salario=(select salario from prueba where nombre='Esquivel Leonel Alfonso') where codigo=3;
Select * from prueba;






