# ¿Qué es sps?

Es un simple escáner de puertos escrito en python, su finalidad es desarrollar un escáner lo más simple posible pero que 
sea completamente funcional y útil.

# ¿Cómo utilizar sps?

Está pensado para utilizarse como un comando pasándole parámetros por lo que debe ser instalado en /usr/bin.
Se ha añadido un script para instalarlo, simplemente ejecute como super usuario:

chmod +x install.sh
./install.sh

Este script simplemente copiará "sps.py" en /usr/bin/sps y le dará permisos de ejecución, en caso de que el script falle puede realizar esta acción usted mismo manualmente.

Tiene dos modos básicos de funcionamiento:

## Modo "common"

El modo "-c" escanea los puertos más utilizados, además proporciona el nombre del servicio que suele estar tras dicho puerto a través de un diccionario, la sintaxis sería:

sps -c ip/host <time>

Ejemplo: sps -c miservidorweb.com 2

Time es un parámetro opcional que se le puede pasar al script para establecer el tiempo en segundos que va a esperar para 
intentar establecer conexión con cada puerto, sino se especifica, por defecto es 1.

## Modo "range"

El modo "-r" escanea los puertos dentro de un rango:

sps -r ip/host puerto_inicial puerto_final <time>

Ejemplo: sps -r miservidorweb.com 10 100 2

En este ejemplo escanearía desde el puerto 10 hasta el 100, notar que en este modo también se puede establecer 
opcionalmente el tiempo de conexión de cada puerto.

# No me colorea la sintaxys ¿Qué hago?

Para que sps funcione correctamente necesita ser ejecutado con python3, con python2 puede presentar problemas al colorear el output.

# ¿Qué licencia usa?

Software liberado con licencia GPLv3.



