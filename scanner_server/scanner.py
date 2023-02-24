import bannergrab as bg
import random as rand
import requests, json
import base64
from enum import Enum

DELTA_DELAY = (0.5,2)
DEFAULT_SCAN = [80, 8000, 8080]
API_POSTADRESS = 'http://127.0.0.1:8000/api/service/'


class IPV4Subnet:
	ip_first = None
	ip_last = None

	def __init__(self, ip_first, ip_last):
		self.ip_first = ip_first
		self.ip_last = ip_last

	@classmethod
	def from_cidr(cls, ip : str, cidr : int):
		ip_bin = [j if jdx < cidr else '0' for jdx, j in enumerate(''.join([f'{int(i):08b}' for i in ip.split('.')]))]
		cls.ip_first = [int(''.join(ip_bin[i:i+8]), 2) for i in range(0,len(ip_bin),8)]
		ip_bin = [j if jdx < cidr else '1' for jdx, j in enumerate(ip_bin)]
		cls.ip_last = [int(''.join(ip_bin[i:i+8]), 2) for i in range(0,len(ip_bin),8)]
		return (cls)
	
	@staticmethod
	def ip_to_int():
		pass

class Scan:
	hosts_batch = list()
	services_founds = list()
	port_list = DEFAULT_SCAN
	url = API_POSTADRESS
	subnet = None

	def __init__(self) -> None:
		pass

	def __init__(self, url : str) -> None:
		self.url = url

	@staticmethod
	def send2api(service_banner : bg.ActiveBannerScanner, url) -> int:
		obj = { 
				'banner' : base64.b64encode(service_banner.banner).decode(),
				'port' : service_banner.port,
				'host' : service_banner.host.ip,
			   }
		req = requests.post(url, data=json.dumps(obj), timeout=2.0)
		return req.status_code
   
	def startscan(self) -> None:
		for port in self.port_list:
			print(f"Looking for services on port {port}.")
			for host in self.hosts_batch:
				host.reqbanner(port)
				if host.service_banners[port].get_dict()['isUp'] == False :
					pass
				if host.service_banners[port].get_dict()['banner'] != '' :
					code = self.send2api(host.service_banners[port], self.url)
					print("Service found at",host.ip," on port ",port)
					if code != 201:
						print("[Error] Request failed to storage server (code=",code,")")
		

	"""
	TODO : Subnet targeted scanning
	"""
	def genbatch_from_mask(self, ip : str, mask : int) -> bool :
		pass
   
	def genbatch_from_rand(self, size=200) -> bool :
		for j in range(size):
			ip = [rand.randint(1,255) for i in range(4)]
			self.hosts_batch.append(bg.Host(''.join([str(ip[i]) + ('.' if i != 3 else '') for i in range(len(ip))])))

	def set_batch(self, batch : list()) -> bool :
		pass

	def set_portlist(self, port_list : list()) -> None:
		for i in port_list :
			if not (i > 0 or i < 65536) :
				raise Exception("Invalid port.")
		self.port_list = port_list