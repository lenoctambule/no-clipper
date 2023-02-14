import socket
import json, requests

RIR_API_URL = 'https://stat.ripe.net/data/address-space-hierarchy/data.json?resource='

class Host:
    ip = "127.0.0.1"
    whois_result = None
    ripe_result = None
    service_banners = dict()

    @staticmethod
    def whois(ip : str) -> dict:
        req = requests.get(RIR_API_URL+ip)
        return json.loads(req.content)

    def __init__(self, ip : str) -> bool:
        self.ip = ip

    def reqbanner(self, port : int) -> bool:
        banner = ActiveBannerScanner(self, port)
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

    def grab_banner(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            res = s.connect_ex((self.host.ip, self.port))
            if res == 0 :
                s.send(b'who_r_u?')
                self.banner = s.recv(1024)
                self.isUp = False 
        self.isUp = True