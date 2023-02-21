import bannergrab as bg
import random as rand
import requests, json

DELTA_DELAY = (0.5,2)
DEFAULT_SCAN = [80, 8000, 8080]
API_POSTADRESS = ['http://localhost:8000/api/add-service']


class Scan:
    hosts_batch = list()
    services_founds = list()
    port_list = DEFAULT_SCAN
    url = API_POSTADRESS

    def __init__(self) -> None:
        pass

    def __init__(self, url : str) -> None:
        self.url = url

    @staticmethod
    def send2api(service_banner : bg.ActiveBannerScanner, url) -> int:
        obj = { 
                'banner' : service_banner.banner.decode(),
                'port' : service_banner.port,
                'host' : service_banner.host.ip,
               }
        req = requests.post(url, data=json.dumps(obj), timeout=2.0)
        return req.status_code
   
    def startscan(self) -> None:
        for port in self.port_list:
            for host in self.hosts_batch:
                host.reqbanner(port)
                if host.service_banners[port].get_dict()['isUp'] == False :
                    pass
                if host.service_banners[port].get_dict()['banner'] != '' :
                    code = self.send2api(host.service_banners[port], self.url)
                    print("Service found at",host.ip," on port ",port)
                    if code != 201:
                        print("[Error] Request failed to storage server (code=",code,")")

    def genbatch_from_mask(self, mask : str) -> bool :
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

