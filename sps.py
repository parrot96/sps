#!/usr/bin/python
# -*- coding: utf-8 -*-

 

"""Copyright 2017 Francisco Dominguez Lerma
 	Author: Francisco Dominguez Lerma

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""


import socket
import sys

common_ports={21:'ftp',22:'ssh',23:'telnet',25:'smtp',53:'dns',135:'NetBios',139:'NetBios',110:'POP3',143:'imap',389:'LDAP',8080:'proxy web',80:'http', 443:'secure http', 9418:'git'}

def scan_range(target, start, end, time=1):
	socket.setdefaulttimeout(time)

	for x in range(start,end+1):
		mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
		try: 
			mi_socket.connect((target, x))
			try:
				print('\033[92m' + "open port -----> " + '\033[0m', x,common_ports[x])
				mi_socket.close()
			except KeyError:
				print('\033[92m' + "open port -----> " + '\033[0m', x)
				mi_socket.close()
		except socket.error:
			mi_socket.close()
	return 0;
def scan_common(target, time=1):

	socket.setdefaulttimeout(time)

	for x in common_ports.keys():
		mi_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			mi_socket.connect((target, x))
			print('\033[92m' + "open port -----> " + '\033[0m', x,common_ports[x])
			mi_socket.close()
		except socket.error:
			mi_socket.close()
	return 0;

def main():
	try:
		if(sys.argv[1]=="--help"):
			print("sps 1.0 version")
			print("USE:")
			print("common ports scan:")
			print("sps -c host/ip timeout(optional)")
			print("range ports scan:")
			print("sps -r host/ip initport endport timeout(optional)")
			exit()
	
		if(sys.argv[1]=="-c"):
			if(len(sys.argv)==4):
				scan_common(sys.argv[2], int(sys.argv[3]))
				exit()
			else:
				scan_common(sys.argv[2])
				exit()
		if(sys.argv[1]=="-r"):
			if(len(sys.argv)==6):
				scan_range(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
				exit()
			else:
				scan_range(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
				exit()
		print("invalid option, please use sps --help")
	except (IndexError, ValueError):
		print("syntax or value error, please use sps --help")

if __name__=="__main__":
	main()
else:
	exit()
