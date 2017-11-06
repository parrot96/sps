#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "You must be a root user"
	exit 1
else
	cp sps.py /usr/bin/sps
	chmod +x /usr/bin/sps
fi

if [ -f /usr/bin/sps ]; then
	echo "sps installed correctly in /usr/bin/sps"
	exit 0
else
	echo "Unexpected ERROR during installation!"
	exit 1
fi
