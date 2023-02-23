import socket
from scapy.all import *
import random as rand

class StealthScanTCP:
	host = None
	port_list = [21,22,23,25,80,443,8000,8080]
	open_ports = list()

	def synreq(self, port):
		packet = IP(dst=self.host)/TCP(sport=rand.randint(25000,65535), dport=port, flags='S')
		return sr1(packet, timeout=0.6, verbose=0)

	def rstreq(self, port):
		packet = IP(dst=self.host)/TCP(sport=rand.randint(25000,65535), dport=port, flags='R')
		return sr1(packet, timeout=0.6, verbose=0)
	
	def __init__(self, host : str) -> None:
		self.host = host
		
	def set_portlist(self, plist : list()) :
		self.port_list = plist

	def startscan(self):
		for port in self.port_list :
			resp = self.synreq(port)
			if resp != None :
				if resp.haslayer(TCP) and resp[TCP].flags == 'SA' :
						self.rstreq(port)
						self.open_ports.append(port)