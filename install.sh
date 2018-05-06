#!/bin/bash

target_path=/usr/local/bin/sps

if [[ $EUID -ne 0 ]]; then
	echo "You must be root"
	exit 1

elif [ -f $target_path ]; then
	echo "sps is already installed in $target_path"
	exit 1
else
	cp sps.py $target_path
	chmod +x $target_path
fi

if [ -f $target_path ]; then
	echo "sps installed correctly in $target_path"
	exit 0
else
	echo "Unexpected ERROR during installation!"
	exit 1
fi
