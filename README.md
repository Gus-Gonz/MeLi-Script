# Para que sirve ??

Este es un script creado para la resolucion de un challenge de Mercado Libre (ARG) en el que se lista los Items en venta para un USER_ID a traves de utilizar la API provista por Mercado Libre.

## Cómo funciona?

Una funcion llamada `get_products_by_id` se encargara de tomar el **USER_ID** introducido por consola y entregarlo a la API , la cual nos devolvera un diccionario con une key llamada **results** la cual posee un Array con los **Id** de cada uno de los productos que dicho vendedor posee en plataforma.

Debido a que solo tenemos el Id de cada producto , se utiliza una Api distinta a la que se le entrega este ID y nos devuelve mas informacion como el nombre y descripcion del producto.

## Por Hacer

[] Al no disponer de una cuenta en Mercado Libre Developer, no se pudo llevar acabo la prueba del script ni poseeo el .log requerido

## Sugerencia

Para futuras practicas alrededor de la API de mercado libre, ellos deberian de entregarnos una cuenta de prueba que nos permita utilizar la API sin problemas.
