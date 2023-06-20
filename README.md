# Ejercicio 1 - Sistema de Alertas

Seguramente conocés la funcionalidad de Notificaciones de Facebook: es esa campanita arriba en el menú donde te muestra las nuevas alertas que el sistema tiene para mostrarte sobre distintos temas: un amigo cumple años, una página que seguís compartió una publicación, un amigo publicó una foto, alguien comentó un posteo tuyo, una sugerencia de amistad, etc.

Facebook no es el único. En general todas las aplicaciones tienen un sistema de alertas o notificaciones. En este ejercicio, te vamos a pedir que hagas una versión muy simplificada.

## Se pide programar un sistema para enviar alertas a usuarios que tenga la siguiente funcionalidad:

1. Se pueden registrar usuarios que recibirán alertas. 

2. Se pueden registrar temas sobre los cuales se enviarán alertas.

3. Los usuarios pueden optar sobre cuales temas quieren recibir alertas.

4. Se puede enviar una alerta sobre un tema y lo reciben todos los usuarios que han optado recibir alertas de ese tema.

5. Se puede enviar una alerta sobre un tema a un usuario específico, solo lo recibe ese único usuario.

6. Una alerta puede tener una fecha y hora de expiración. 

7. Hay dos tipos de alertas: Informativas y Urgentes.

8. Un usuario puede marcar una alerta como leída.

9. Se pueden obtener todas las alertas no expiradas de un usuario que aún no ha leído. 

10. Se pueden obtener todas las alertas no expiradas para un tema. Se informa para cada alerta si es para todos los usuarios o para uno específico.

11. Tanto para el punto `9` como el `10`, el ordenamiento de las alertas es el siguiente: las Urgentes van al inicio, siendo la última en llegar la primera en obtenerse `(LIFO)`. Y a continuación las informativas, siendo la primera en llegar la primera en obtenerse `(FIFO)`.

    Ej: Dadas las siguientes alertas Informativas y Urgentes que llegan en el siguiente orden: `I1,I2,U1,I3,U2,I4` se ordenarán de la siguiente forma --> `U2,U1,I1,I2,I3,I4`


## Aclaraciones importantes:

1.  La aplicación se ejecuta desde línea de comando. En ningún caso pedimos que escribas código de front end, tampoco que hagas     impresiones a la consola.

2. Debe tener Tests Unitarios.

3. No debés hacer ningún tipo de persistencia de datos (base de datos, archivos). Todo debe resolverse con estructuras en memoria.

4. Si tenés que hacer algún supuesto sobre algo que no esté claro en el ejercicio, por favor anotalo para que lo tengamos en cuenta al revisar el código.

5. Al responder el ejercicio, por favor entregá código que funcione y se pueda probar. Se minucioso en los detalles y en la claridad del código que escribas para que al revisor le sea fácil entenderlo. 

## Cuando revisamos el ejercicio, esto es lo que evaluamos:

1. Solución: ¿El código soluciona correctamente los requisitos? 
2. Programación orientada a objetos: 
    a. ¿Hay un modelo de clases pensado, que modela la realidad del enunciado? 
    b. ¿Está resuelto usando polimorfismo?
    c. ¿Hay algún patrón de diseño presente en la solución?

## Explicacion con respecto a la resolucion del codigo y como tome cada punto de requerimiento

1. tome el punto 1 como "un usuario puede desactivar notificaciones de manera global"

2. hice una clase Subject(Tema) donde cualquier usuario se puede registrar, por lo que entendi del ejercicio, solo se envian alertas de subjects.

3. aca hice un sistema donde un usuario se registra a un tema pero puede tener las notificaciones desactivadas.

4. una clase alerta puede enviar a todos los usurios registrados a ese tema que tengan notificaciones activadas el mensaje.

5. la clase alerta puede enviar mensajes a un solo usuario registrado a un subject

6. creation date se crea cuando se instancia la clase, expiration date se debe settear

7. la clase alert la tome como clase padre, pero donde realmente se crean las clases en el informative alert y urgent alert

8. en la clase user alerts existe esa funcionalidad

9. idem al 8

11. no cree un algoritmo como tal, pense el codigo en donde siempre se van a crear alertas en este sistema y no llegara de sistemas externos. Entonces la estructura `lifo`para alertas urgentes lo maneja la clase urgent alerts donde la agrega al principio de la lista. La estructura `fifo`lo hace la clase info alerts, donde agrega la alerta al final de la lista de alertas no leidas del usuario


# Ejercicio 2 - Consulta SQL

## Escribir una consulta SQL que traiga todos los clientes que han comprado en total más de 100,000$ en los últimos 12 meses usando las siguientes tablas: 

`Clientes: ID, Nombre, Apellido`

`Ventas: Fecha, Sucursal, Numero_factura, Importe, Id_cliente`

## Resolucion

Use: [OneCompiler](https://onecompiler.com/mysql/)

1. utilizando el siguiente setup de tablas con algunos campos creados

```
CREATE TABLE Clientes (
  ID INTEGER PRIMARY KEY,
  Nombre varchar(100), 
  Apellido varchar(100)
);
insert into Clientes (ID, Nombre, Apellido) values (1, 'albert', 'einstein');
insert into Clientes (ID, Nombre, Apellido) values (2, 'isaac', 'newton');
insert into Clientes (ID, Nombre, Apellido) values (3, 'marie', 'curie');

CREATE TABLE Ventas (
  Fecha DATE,
  Sucursal VARCHAR(50),
  Numero_factura INT,
  Importe DECIMAL(10,2),
  Id_cliente INT,
  PRIMARY KEY (Numero_factura),
  FOREIGN KEY (Id_cliente) REFERENCES Clientes(ID)
);

INSERT INTO Ventas (Fecha, Sucursal, Numero_factura, Importe, Id_cliente) values ('2020-06-01', 'Sucursal A', 1, 150000.00, 1);
INSERT INTO Ventas (Fecha, Sucursal, Numero_factura, Importe, Id_cliente) values ('2023-06-05', 'Sucursal B', 2, 250000.00, 2);
INSERT INTO Ventas (Fecha, Sucursal, Numero_factura, Importe, Id_cliente) values ('2023-06-10', 'Sucursal A', 3, 120.50, 3);
```

2. ejecuta la siguiente query

```
SELECT ID, Nombre, Apellido
FROM Clientes 
JOIN Ventas ON ID = Id_cliente
WHERE Fecha >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
GROUP BY ID, Nombre, Apellido
HAVING SUM(Importe) > 100000;
```

### NOTA: En la `QUERY`, si al `SELECT` y al `GROUPBY` se le agrega `Importe` al final, va a mostrar el importe tambien