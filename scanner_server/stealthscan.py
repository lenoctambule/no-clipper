import socket
from scapy.all import *
import random as rand

class StealthScanTCP:
	host = None
	port_list = [21,22,23,25,80,443,8000,8080]
	open_ports = list()

	def sendflag(self, port : int, flag : str ,timeout=0.7):
		packet = IP(dst=self.host)/TCP(sport=rand.randint(25000,65535), dport=port, flags=flag)
		return sr1(packet, timeout=timeout, verbose=0)
	
	def __init__(self, host : str) -> None:
		self.host = host
		
	def set_portlist(self, plist : list()) :
		self.port_list = plist

	def startscan(self):
		for port in self.port_list :
			resp = self.synreq(port, 'S')
			if resp != None :
				if resp.haslayer(TCP) and resp[TCP].flags == 'SA' :
						self.rstreq(port, 'R')
						self.open_ports.append(port)