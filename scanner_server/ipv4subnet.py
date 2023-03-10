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