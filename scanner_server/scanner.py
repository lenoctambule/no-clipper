import bannergrab as bg
import random as rand
import requests, sys

DELTA_DELAY = (0.5,2)
DEFAULT_SCAN = [80, 8000, 8080]
API_POSTADRESS = ['http://localhost:8000/api/add-service']
HELP_MESSAGE = "Usage : python scanner.py <batch_size> <url>"
DEBUG_MSGS = {'init' : "Initalising scan ...", 
                'start' : "Scan initialized\n[Scan running] \nPress Ctrl+C to stop" }

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
                'host' : service_banner.host.ip, 
                'banner' : service_banner.banner,
                'port' : service_banner.port,
               }
        try :
            req = requests.post(url, data=obj, timeout=2.0)
        except :
            return 0
        return req
   
    def startscan(self) -> None:
        for port in self.port_list:
            for host in self.hosts_batch:
                host.reqbanner(port)
                if host.service_banners[port].get_dict()['isUp'] == False :
                    pass
                if host.service_banners[port].get_dict()['banner'] != '' :
                    code = self.send2api(host)
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

if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print(HELP_MESSAGE)
        exit(0)
    batch_size = None
    api_url = None

    try :
        batch_size = int(sys.argv[1])
        api_url = sys.argv[2]
    except :
        print("Invalid args. \n",HELP_MESSAGE)
        exit(0)

    print(DEBUG_MSGS['init'])
    scan = Scan(api_url)
    scan.genbatch_from_rand(batch_size)

    print(DEBUG_MSGS['start'])
    while (1):
        scan.startscan()
        scan.genbatch_from_rand(batch_size)
