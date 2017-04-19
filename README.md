# ¿Qué es sps?

Es un simple escáner de puertos escrito en python, su finalidad es desarrollar un escáner lo más simple posible pero que 
sea completamente funcional y útil.

# ¿Cómo utilizar sps?

Está pensado para utilizarse como un comando pasándole parámetros, una vez el fichero "sps.py" esté hubicado en algura ruta 
para poder ser ejecutado como "/usr/bin" y habiéndole dado permisos de ejecución, podremos hacer uso de él.

Tiene dos modos básicos de funcionamiento:

## El modo "-c" escanea los puertos más utilizados, además proporciona el nombre del servicio que suele estar tras dicho puerto a través de un diccionario, la sintaxis sería:

sps -c ip/host <time>

Ejemplo: sps -c miservidorweb.com 2

Time es un parámetro opcional que se le puede pasar al script para establecer el tiempo en segundos que va a esperar para 
intentar establecer conexión con cada puerto, sino se especifica, por defecto es 1.

## El modo "-r" escanea los puertos dentro de un rango:

sps -r ip/host puerto_inicial puerto_final <time>

Ejemplo: sps -r miservidorweb.com 10 100 2

En este ejemplo escanearía desde el puerto 10 hasta el 100, notar que en este modo también se puede establecer 
opcionalmente el tiempo de conexión de cada puerto.

# ¿Qué licencia usa?

Es software liberado con la licencia GPLv3.



