<h1 align="center"> FunkosShop </h1>

![FunkosShop-Logo](https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/75abfc47-f06e-4bc5-9aeb-d0ece8d78d99)

## Descripción del proyecto

Estamos creando una pagina web donde nuestros usuarios podrán registrarse y comprar nuestros productos

## Autores

| [<img src="https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/c7c718ff-d09c-40ee-a00c-638b2a3bca10" width=115><br><sub>David Ortiz Corchero</sub>](https://github.com/DavidOrtizz) | [<img src="https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/d882a8f4-fb83-4082-88ae-6cd7bbc11531" width=115><br><sub>Alejandro Moreno Garrido</sub>](https://github.com/AMorGar) | [<img src="https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/ae31b535-a8f9-4d60-8e22-4ca2df539bad" width=115><br><sub>Ionut Grigore Pop</sub>](https://github.com/popionut) | [<img src="https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/c4182359-f246-4c71-bd65-324adc6d1411" width=115><br><sub>Pablo Frías Campos</sub>](https://github.com/PabloFriasCampos) |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |

## ¿Que ha realizado cada uno?

![Nuestra base de datos](https://github.com/DavidOrtizz/ProyectoConFlask/assets/116579416/c2dd320c-394f-45b6-ae19-fa564cc83701)
<br>
**Alejandro** <br>
Ha realizado la creación de la SEDE
<br>
**Ionut** <br>
Ha realizado la creación de PEDIDO
<br>
**Pablo** <br>
Ha realizado la creación de OPERARIO, con 5 endpoints, y la creación y configuración de un mini-frontend con angular y el uso de un fichero log. <br>
**ENDPOINTS OPERARIO** <br>

## GET /operario <br>

Este endpoint devuelve todos los operarios de la base de datos, los cuales tienen el rol de "Usuario"

## GET /operario/OperarioID <br>

Este endpoint devuelve todos los datos del operario indicado por ID

## POST /operario <br>

Este endpoint se utiliza para crear un operario (Los datos se mandan por json)

## PUT /operario/OperarioID <br>

Este endpoint modifica los datos del operario indicado por ID

## DELETE /operario/OperarioID <br>

Este endpoint borra el operario indicado por ID
<br>
**David** <br>
Ha realizado la creación de PRODUCTO
<br>

## CÓDIGO SQLITE PARA BASE DE DATOS

-- Create OPERARIO table
CREATE TABLE OPERARIO (
OperarioID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre VARCHAR(50),
Direccion VARCHAR(70),
Rol VARCHAR(15) CHECK(Rol IN ('Usuario', 'Administrador')),
SedeID INTEGER REFERENCES SEDE(SedeID)
);
-- Create PEDIDO table
CREATE TABLE PEDIDO (
PedidoID INTEGER PRIMARY KEY AUTOINCREMENT,
OperarioID INTEGER REFERENCES OPERARIO(OperarioID),
TotalPedidoEUR DECIMAL,
Pagado BOOLEAN
);
-- Create LISTA_PRODUCTO_PEDIDO table
CREATE TABLE LISTA_PRODUCTO_PEDIDO (
PedidoProductoID INTEGER PRIMARY KEY AUTOINCREMENT,
ProductoID INTEGER REFERENCES PRODUCTO(ProductoID),
PedidoID INTEGER REFERENCES PEDIDO(PedidoID),
Cantidad INTEGER,
TotalProductoEUR DECIMAL
);
-- Create PRODUCTO table
CREATE TABLE PRODUCTO (
ProductoID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre VARCHAR(50),
PrecioEUR DECIMAL,
Descripcion TEXT,
StockDisponible INTEGER
);
-- Create SEDE table
CREATE TABLE SEDE (
SedeID INTEGER PRIMARY KEY AUTOINCREMENT,
Direccion VARCHAR(70),
NIF VARCHAR(10)
);
