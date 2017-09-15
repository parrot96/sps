#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "You must be a root user"
	exit 1
else
	cp sps.py /usr/bin/sps
	chmod +x /usr/bin/sps
fi

if [ -f /usr/bin/sps ]; then
	echo "sps instalado con éxito en /usr/bin/sps"
	exit 0
else
	echo "¡ERROR inesperado durante la instalación!"
fi
