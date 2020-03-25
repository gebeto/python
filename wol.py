#!/usr/bin/env python

import socket
import sys


def wake(ip, port, mac):
	data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(data.decode("hex"), (ip, port))

wake(*sys.argv)
