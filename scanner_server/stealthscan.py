import socket
from scapy.all import *
import random as rand
import requests, json

class StealthScanTCP:
	host = None
	port_list = [21,22,23,25,80,389,636,443,8000,8080,8888]
	open_ports = None

	def sendflag(self, port : int, flag : str ,timeout=1):
		packet = IP(dst=self.host)/TCP(sport=rand.randint(25000,65535), dport=port, flags=flag)
		return sr1(packet, timeout=timeout, verbose=0)
	
	def __init__(self, host : str) -> None:
		self.host = host
		self.open_ports = list()
		
	def set_portlist(self, plist : list()) :
		self.port_list = plist

	def check_port(self, port : int):
		resp = self.sendflag(port, 'S')
		if resp != None :
			if resp[IP].src == self.host and resp.haslayer(TCP) and resp[TCP].flags == 'SA' :
				self.sendflag(port, 'R')
				self.open_ports.append(port)
				print('Found running service on port '+str(port))

	def send2api(self, api_url):
		obj = {'ip': self.host,
	 			'open_ports': ''.join([str(self.open_ports[i])+ (',' if i != len(self.open_ports) -1 else '') for i in range(len(self.open_ports))])}
		req = requests.post(api_url+'api/host/', data=json.dumps(obj))
		return req.status_code

	def startscan(self):
		threads = list()
		for i in self.port_list:
			t = threading.Thread(target=self.check_port, args=[i])
			t.daemon = True
			threads.append(t)
		for t in threads :
			t.start()
		for t in threads :
			t.join()


class MassScan:
	hosts = list()
	api_url = None

	def __init__(self, api_url='http://127.0.0.1:8000/',size=200) -> None :
		self.api_url = api_url
		for j in range(size):
			ip = [rand.randint(1,255) for i in range(4)]
			self.hosts.append(StealthScanTCP(''.join([str(ip[i]) + ('.' if i != 3 else '') for i in range(len(ip))])))

	def scan(self):
		for i in self.hosts:
			print('Scanning',i.host)
			i.startscan()
			i.send2api(self.api_url)

while True :
	s = MassScan(size=2000)
	s.scan()
