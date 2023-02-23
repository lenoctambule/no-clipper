import socket
import json, requests

RIR_API_URL = 'https://stat.ripe.net/data/address-space-hierarchy/data.json?resource='
HTTP_GETREQ = b'GET / HTTP/1.1\r\n'

class Host:
	ip = "127.0.0.1"
	whois_result = None
	ripe_result = None
	service_banners = dict()

	@staticmethod
	def whois(ip : str) -> dict:
		req = requests.get(RIR_API_URL+ip)
		return json.loads(req.content)

	def __init__(self, ip : str) -> None:
		self.ip = ip

	def reqbanner(self, port : int) -> bool:
		banner = ActiveBannerScanner(self, port)
		banner.grab_banner()
		self.service_banners[port] = banner

	def reqwhois(self) -> None:
		self.whois_result = self.whois(self.ip)

class ActiveBannerScanner:
	banner = ""
	service = ""
	port = 80
	host = None
	isUp = False

	def __init__(self, host : Host, port : int) -> None:
		socket.setdefaulttimeout(1)
		self.port = port
		self.host = host

	def __str__(self) -> str:
		return str({ 'port' : self.port, 
		'banner' : self.banner ,
		'service' : self.service,
		'host' : self.host.ip,
		'isUp' : self.isUp})
	
	def get_dict(self) -> dict:
		return { 'port' : self.port, 
		'banner' : self.banner ,
		'service' : self.service,
		'host' : self.host.ip,
		'isUp' : self.isUp}
	
	@staticmethod
	def recvall(s):
		BUFF_SIZE = 4096
		data = b''
		while True:
			part = s.recv(BUFF_SIZE)
			data += part
			if len(part) < BUFF_SIZE:
				break
		return data

	def grab_banner(self):
		with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
			res = s.connect_ex((self.host.ip, self.port))
			if res == 0 :
				s.send(HTTP_GETREQ+b'Host:'+self.host.ip.encode()+b'\r\n\r\n')
				try :
					self.banner = self.recvall(s)
				except :
					pass
				self.isUp = True
			else :
				self.isUp = False